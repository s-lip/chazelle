import datetime

from django.shortcuts import render
from django.http import Http404

from django.conf import settings

from teams.models import Team
from rounds.models import Round

def hunt_has_started():
    return datetime.datetime.now() > settings.HUNT_START_TIME
    
def hunt_active(view):
    '''Checks if the hunt has started yet; if not, directs you to the countdown page'''
    def new_view(*args):
        if hunt_has_started() or settings.HUNT_STARTED:
            return view(*args)
        else:
            request = args[0]
            return render(request, 'countdown.html', { 'start_time': settings.HUNT_START_TIME })
    return new_view
            
def is_unlocked(view):
    '''Checks to see if this round is unlocked for this team; if not, 404s'''
    def new_view(request, round_slug):
        team = Team.objects.get(id=request.user.id)
        if team.rounds_unlocked.filter(slug=round_slug):
            return view(request, round_slug)
        else:
            raise Http404
    return new_view
        
    
def next_autounlock_time(team):
    '''When the next round will unlock, regardless of solve speed. Currently really dumb.'''
    available_rounds = team.rounds_unlocked.count()
    last_unlock = team.last_unlock
    return last_unlock + datetime.timedelta(hours=3)
    

def rounds_remain(team):
    '''Returns True if there are still rounds this team hasn't unlocked'''
    return Round.objects.count() > team.rounds_unlocked.count()
    
    
def shall_we_unlock(team):
    '''Decides whether or not to unlock more rounds based on team's current progress. Kinda dumb.'''
    if datetime.datetime.now() > next_autounlock_time(team):
        return True
        
    # if there are more rounds to solve
    if rounds_remain():
        available_rounds = team.rounds_unlocked.all()
        solved_rounds = []
        for round in team.rounds_unlocked.all():
            # have we solved a given round's supermeta or whatever
            if round.puzzle_set.get(is_roundsolution=True) in team.puzzles_solved.filter(round=round):
                solved_rounds.append(round)
      
        # if all available rounds have had their supermeta solved
        if len(solved_rounds) == available_rounds.count():
            return True
        
        # how many puzzles haven't we solved yet?
        unsolved_puzzle_count = 0
        # how many puzzles are unsolved in unsolved rounds? (excludes puzzles to be backsolved)
        unsolved_puzzle_in_unsolved_round_count = 0
        for round in available_rounds:
            remaining_puzzles = list(set(round.puzzle_set.all()) - set(team.puzzles_solved.filter(round=round)))
            unsolved_puzzle_count += len(remaining_puzzles)
            if round in solved_rounds:
                unsolved_puzzle_in_unsolved_round_count += len(remaining_puzzles)
        
        # only one round left            
        if len(solved_rounds) == available_rounds.count() - 1 and unsolved_puzzle_in_unsolved_round_count < 5:
            return True
            
        if unsolved_puzzle_count < 10:
            return True
        
    return False
    
    
def post_solution_unlock(team):
    '''Runs after each puzzle solve, to see if we should unlock more puzzles'''
    if shall_we_unlock(team):
        unlock_next_round(team)
        
def auto_unlock(team):
    '''Checks autounlock time, and autounlocks if appropriate. This should be run by a cron job or something'''
    if rounds_remain() and datetime.datetime.now() > next_autounlock_time(team):
        unlock_next_round(team)
        
def unlock_next_round(team):
    '''Unlock the next round. Assumes rounds have order.'''
    available_rounds = team.rounds_unlocked.count()
    try:
        next_round = Round.objects.get(order=available_rounds+1)
        team.rounds_unlocked.add(next_round)
        team.last_unlock = datetime.datetime.now()
        team.save()
    except DoesNotExist:
        # looks like there aren't any more rounds to unlock, so let's confirm that
        if not rounds_remain():
            team.rounds_unlocked = Round.objects.all()

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rounds.game_controller import hunt_active, next_autounlock_time

from teams.models import Team

@hunt_active
@login_required
def home(request):
    team = Team.objects.get(id=request.user.id)
    context = {
        'available_rounds': team.rounds_unlocked.all()
    }
    return render(request, 'index.html', add_nav_context(request, context))
    

@login_required  
def notes(request):
    return render(request, 'notes/index.html', add_nav_context(request, {}))
    

@login_required  
def note(request, note_name):
    return render(request, 'notes/' + note_name + '.html', add_nav_context(request, {}))


def add_nav_context(request, context):
    team = Team.objects.get(id=request.user.id)
    nav_context = {
        'team': team,
        'next_unlock_time': next_autounlock_time(team)
    }
    return dict(nav_context.items() + context.items())

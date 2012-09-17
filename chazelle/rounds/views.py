from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rounds.game_controller import is_unlocked

from hunt.views import add_nav_context

@is_unlocked
@login_required
def round(request, round_slug):
    context = { 
        'round_slug': round_slug 
        }
    return render(request, round_slug + '/index.html', add_nav_context(request, context))

@is_unlocked
@login_required 
def puzzle(request, round_slug, puzzle_slug):
    print request.user.name
    print request.user.extra_credit
    
    is_solved = False
    if request.user.puzzles_solved.filter(slug=puzzle_slug):
        is_solved = True
    context = { 
        'round_slug': round_slug, 
        'puzzle_slug': puzzle_slug, 
        'is_solved' : is_solved 
        }
        
    return render(request, round_slug + '/' + puzzle_slug + '.html', add_nav_context(request, context))


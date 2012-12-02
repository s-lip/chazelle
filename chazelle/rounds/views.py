from django.shortcuts import render
from hunt.hunt_state import state

from hunt.views import add_nav_context

def round(request, round_slug):
    context = { 
        'round_slug': round_slug 
        }
    return render(request, 'rounds/' + round_slug + '/index.html', add_nav_context(request, context))

def puzzle(request, round_slug, puzzle_slug):
    is_solved = False
    context = { 
        'round_slug': round_slug, 
        'puzzle_slug': puzzle_slug, 
        'is_solved' : is_solved 
        }
        
    return render(request, 'rounds/' + round_slug + '/' + puzzle_slug + '.html', add_nav_context(request, context))


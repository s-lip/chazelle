from django.shortcuts import render
import hunt.hunt_state

def round(request, round_slug):
    context = hunt.hunt_state.HuntState().get_context(
        general_data=['team'],
        injected_data=[round_slug]) 
    print context
    return render(request, 'rounds/' + round_slug + '/index.html', context)

def puzzle(request, round_slug, puzzle_slug):
    is_solved = False
    context = { 
        'round_slug': round_slug, 
        'puzzle_slug': puzzle_slug, 
        'is_solved' : is_solved 
        }
        
    return render(request, 'rounds/' + round_slug + '/' + puzzle_slug + '.html', context)


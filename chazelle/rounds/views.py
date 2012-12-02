from django.shortcuts import render

def round(request, round_slug):
    context = { 
        'round_slug': round_slug 
        }
    return render(request, 'rounds/' + round_slug + '/index.html', context)

def puzzle(request, round_slug, puzzle_slug):
    is_solved = False
    context = { 
        'round_slug': round_slug, 
        'puzzle_slug': puzzle_slug, 
        'is_solved' : is_solved 
        }
        
    return render(request, 'rounds/' + round_slug + '/' + puzzle_slug + '.html', context)


from django.shortcuts import render
from hunt.hunt_state import state

def home(request):
    team = state['team']
    context = {
        'rounds': state['rounds'],
    }
    return render(request, 'index.html', add_nav_context(request, context))
    
 
def notes(request):
    return render(request, 'notes/index.html', add_nav_context(request, {}))
    

def note(request, note_name):
    return render(request, 'notes/' + note_name + '.html', add_nav_context(request, {}))


def add_nav_context(request, context):
    team = state['team']
    nav_context = {
        'team': team,
        'next_unlock_time': state['next_autounlock_time']
    }
    return dict(nav_context.items() + context.items())

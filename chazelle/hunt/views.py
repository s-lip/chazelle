from django.shortcuts import render
from hunt.hunt_state import state, HuntState

def home(request):
    context = HuntState().for_home()
    return render(request, 'index.html', add_nav_context(request, context))


def notes(request):
    return render(request, 'notes/index.html', add_nav_context(request, {}))


def note(request, note_name):
    return render(request, 'notes/' + note_name + '.html', add_nav_context(request, {}))


def add_nav_context(request, context):
    nav_context = {
        'team': state['team'],
        'next_unlock_time': state['next_autounlock_time']
    }
    for round in state['rounds']:
        nav_context[round.slug] = round

    poster_string = 'poster'
    for round in state['rounds']:
        if round.is_solved:
            poster_string = poster_string + '-' + round.slug
    nav_context['poster'] = poster_string + '.png'
    return dict(nav_context.items() + context.items())

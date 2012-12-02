from django.shortcuts import render
from hunt.hunt_state import state, HuntState

def home(request):
    context = HuntState().get_context(
        general_data=['team'],
        injected_data=['rounds'])
    return render(request, 'index.html', context)


def notes(request):
    context = HuntState().get_context(
        general_data=['team'])
    return render(request, 'notes/index.html', context)


def note(request, note_name):
    context = {}
    return render(request, 'notes/' + note_name + '.html', context)

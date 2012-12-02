from django.shortcuts import render
import hunt.hunt_state

def home(request):
    context = hunt.hunt_state.HuntState().get_context(
        general_data=['team'],
        injected_data=['rounds'])
    return render(request, 'index.html', context)


def notes(request):
    context = hunt.hunt_state.HuntState().get_context(
        general_data=['team'])
    return render(request, 'notes/index.html', context)


def note(request, note_name):
    context = hunt.hunt_state.HuntState().get_context(
        general_data=['team'])
    return render(request, 'notes/' + note_name + '.html', context)

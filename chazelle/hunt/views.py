from django.shortcuts import render
import hunt.hunt_state
import os.path
import django.http

def get_url_with_cache(u):
    import httplib2 # optional dependency
    h = httplib2.Http(os.path.expanduser("~/.httplibcache/"))
    resp, content = h.request(u, "GET")
    return content

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

def postprod(request):
    puzzle_html = get_url_with_cache(request.GET['htmlurl'])
    if not request.GET['sekrit'] == 'supersekrit':
        assert request.COOKIES['PHPSESSID'] # basic for now
    return django.http.HttpResponse(puzzle_html)

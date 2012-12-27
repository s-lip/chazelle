from django.shortcuts import render
import hunt.hunt_state
import os.path
import django.http
import urllib

def get_url_with_cache(u):
    import httplib2 # optional dependency
    h = httplib2.Http(os.path.expanduser("~/.httplibcache/"))
    resp, content = h.request(u, "GET")
    return content

def session_id_looks_good(cookie_dict):
    import httplib2 # optional dependency
    url = "http://z.manicsages.org/puzzle/login.php"

    cookie_dict_as_string = urllib.urlencode(cookie_dict)
    h = httplib2.Http(os.path.expanduser("~/.httplibcache/"))
    resp, content = h.request(url, "GET",
                              headers={'Cookie': cookie_dict_as_string})
    return ("You are logged in. Would you like to" in content)

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
    if request.GET.get('sekrit', '') == 'supersekrit':
        pass # yay back door
    else:
        assert session_id_looks_good(request.COOKIES)
    return django.http.HttpResponse(puzzle_html)

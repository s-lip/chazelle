from django.shortcuts import render
import hunt.hunt_state
import os.path
import django.http
import urllib
import rounds.views
import django.utils.safestring


def get_url_with_cache(u):
    import httplib2 # optional dependency
    h = httplib2.Http(os.path.expanduser("~/.httplibcache/"))
    resp, content = h.request(u, "GET")
    return content


def session_id_looks_good(cookie_dict):
    import httplib2 # optional dependency
    url = "http://z.manicsages.org/puzzle/login.php"

    cookie_dict_as_string = urllib.urlencode(cookie_dict)
    h = httplib2.Http()
    resp, content = h.request(url, "GET",
                              headers={'Cookie': cookie_dict_as_string})
    return ("You are logged in. Would you like to" in content)


def home(request):
    context = hunt.hunt_state.HuntState().get_context(
        general_data=['team', 'notes'],
        injected_data=['rounds'])
    return render(request, 'index.html', context)


def notes(request):
    context = hunt.hunt_state.HuntState().get_context(
        general_data=['team', 'notes'])
    return render(request, 'notes/index.html', context)


def note(request, note_name):
    context = hunt.hunt_state.HuntState().get_context(
        general_data=['team'])
    return render(request, 'notes/' + note_name + '.html', context)

def postprod(request):
    if request.GET.get('sekrit', '') == 'supersekrit':
        pass # yay back door
    else:
        phpsessid = request.COOKIES.get('PHPSESSID', '')
        if not phpsessid:
            import logging
            logging.error("YOWEE why no session iD")

        if session_id_looks_good({'PHPSESSID': phpsessid}):
            pass
        else:
            logging.error("WEIRD failed for %s", phpsessid)
            return django.http.HttpResponse("You seem not to be logged in to puzzletron.")

    import lxml.html # optional dependency
    url = request.GET['htmlurl'] + '/index.html'
    data = get_url_with_cache(url)
    as_tags = lxml.html.fromstring(data)
    # make links and images reference the base url
    as_tags.make_links_absolute(base_url=url, resolve_base_href=False)
    puzzle_html = django.utils.safestring.SafeString(lxml.html.tostring(as_tags))
    round_full = request.GET.get('roundname', '')
    round_full2slug = {
        'Agent 99': None, # FIXME
        'Sneakers': 'sneakers',
        'Rubik': 'rubik',
        'Feynman': 'feynman',
        "Ocean's 11": 'oceans_11',
        'Get Smart': 'get_smart',
        'Indiana Jones': 'indiana',
        }

    round_slug = round_full2slug[round_full]

    return rounds.views.puzzle(request=request,
                               round_slug=round_slug,
                               puzzle_slug='puzzle',
                               extra_context={'body': puzzle_html,
                                              'puzzle_name':
                                                  request.GET.get('title', ''),
                                              })
    return django.http.HttpResponse(puzzle_html)

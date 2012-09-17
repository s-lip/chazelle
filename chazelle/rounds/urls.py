from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<round_slug>[\w_]+)/$', 'rounds.views.round', name='round'),
    url(r'^(?P<round_slug>[\w_]+)/(?P<puzzle_slug>[\w_]+)/$', 'rounds.views.puzzle', name='puzzle'),
)

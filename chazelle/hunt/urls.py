from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hunt.views.home', name='home'),
    url(r'^notes/$', 'hunt.views.notes', name='notes'),
    url(r'^notes/(?P<note_name>[\w_]+)/$', 'hunt.views.note', name='note'),
    url(r'^rounds/', include('rounds.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',  name='django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^admin/', include(admin.site.urls)),
)

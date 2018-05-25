from django.conf.urls import *

urlpatterns = ['',
    url('^login/$', 'googleauth.views.login', name='googleauth_login'),
    url('^callback/$', 'googleauth.views.callback', name='googleauth_callback'),
    url('^logout/$', 'googleauth.views.logout', name='googleauth_logout'),
]
from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^$', dashboard_home_page, name='dashboard_home_page'),

    url(r'^messages/$', liste_messages, name='liste_messages_recu'),
    url(r'^messages/(?P<pk>[0-9]+)/details$', details_message, name='message_details'),
    url(r'^messages/new/$', ecrire_message, name='ecrire_message'),
    url(r'^messages/(?P<pk>[0-9]+)/edit/$', modifier_message, name='modifier_message'),
    url(r'^reponse/(?P<pk>\d+)/repondre/$', repondre_message, name='repondre_message'),

    url(r'^inscriptions/', include('inscriptions.urls')),

    url(r'^modules/', include('modules.urls')),

]

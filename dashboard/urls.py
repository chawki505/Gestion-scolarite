from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^$', dashboard_home_page, name='dashboard_home_page'),

    url(r'^liste_inscriptions/$', dashboard_liste_inscriptions, name='dashboard_liste_inscriptions'),
    url(r'^liste_etudiants/$', dashboard_liste_etudiants, name='dashboard_liste_etudiants'),
    url(r'^liste_bacs/$', dashboard_liste_bac, name='dashboard_liste_bacs'),

    url(r'^(?P<pk>[0-9]+)/$', dashboard_detail_inscription, name='dashboard_detail_inscription'),

    url(r'^attestation/', include('inscriptions.urls'))
]

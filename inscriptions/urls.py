from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^liste_inscriptions/$', dashboard_liste_inscriptions, name='dashboard_liste_inscriptions'),

    url(r'^liste_etudiants/$', dashboard_liste_etudiants, name='dashboard_liste_etudiants'),

    url(r'^liste_bacs/$', dashboard_liste_bac, name='dashboard_liste_bacs'),

    url(r'^liste_inscriptions/detail/(?P<pk>[0-9]+)/$', dashboard_detail_inscription,
        name='dashboard_detail_inscription'),

    url(r'^liste_etudiants/detail/(?P<pk>[0-9]+)/$', dashboard_detail_etudiant,
        name='dashboard_detail_etudiant'),

    url(r'^attestation_inscription/(?P<pk>[0-9]+)/$', attestation_inscription, name='attestation_inscription'),

    url(r'^certificat_scolarite/(?P<pk>[0-9]+)/$', certificat_scolarite, name='certificat_scolarite'),

]

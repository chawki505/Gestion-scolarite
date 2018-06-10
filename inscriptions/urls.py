from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^liste_inscriptions/$',
        dashboard_liste_inscriptions,
        name='dashboard_liste_inscriptions'),

    url(r'^liste_inscriptions/(?P<pk>[0-9]+)/detail$',
        dashboard_detail_inscription,
        name='dashboard_detail_inscription'),

    url(r'^liste_inscriptions/(?P<pk>[0-9]+)/detail/attestation_inscription/$',
        attestation_inscription,
        name='attestation_inscription'),

    url(r'^liste_inscriptions/(?P<pk>[0-9]+)/detail/certificat_scolarite/$',
        certificat_scolarite,
        name='certificat_scolarite'),

    url(r'^liste_etudiants/$',
        dashboard_liste_etudiants,
        name='dashboard_liste_etudiants'),

    url(r'^liste_etudiants/(?P<pk>[0-9]+)/detail$',
        dashboard_detail_etudiant,
        name='dashboard_detail_etudiant'),

    url(r'^liste_bacs/$',
        dashboard_liste_bac,
        name='dashboard_liste_bacs'),




    url(r'^etudiant/(?P<pk>[0-9]+)/information',
        dashboard_etudiant_information,
        name='dashboard_etudiant_information'),

    url(r'^etudiant/(?P<pk>[0-9]+)/historique$',
        dashboard_etudiant_historique,
        name='dashboard_etudiant_historique'),

    url(r'^etudiant/(?P<pk>[0-9]+)/parcours',
        dashboard_etudiant_parcours,
        name='dashboard_etudiant_parcours'),

]

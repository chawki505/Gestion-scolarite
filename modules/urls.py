from django.conf.urls import url, include

from .views import *

urlpatterns = [

    url(r'^liste_modules/$',
        liste_modules,
        name='liste_modules'),

    url(r'^liste_modules/(?P<pk>[0-9]+)/$',
        liste_notes_module,
        name='liste_notes_module'),

    url(r'^liste_modules/(?P<pk>[0-9]+)/pv$',
        pv_module,
        name='pv_module'),




    url(r'^liste_unites/$',
        liste_unites,
        name='liste_unites'),

    url(r'^liste_unites/(?P<pk>[0-9]+)/$',
        liste_notes_unite,
        name='liste_notes_unite'),

    url(r'^liste_unites/(?P<pk>[0-9]+)/pv$',
        pv_unite,
        name='pv_unite'),





    url(r'^liste_semestre/$',
        liste_semestres,
        name='liste_semestre'),

    url(r'^liste_semestre/(?P<pk>[0-9]+)/$',
        liste_notes_semestre,
        name='liste_notes_semestre'),

    url(r'^liste_semestre/(?P<pk>[0-9]+)/pv$',
        pv_semestre,
        name='pv_semestre'),

]

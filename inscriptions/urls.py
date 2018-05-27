from django.conf.urls import url
from .views import attestation_inscription

urlpatterns = [

    url(r'^(?P<pk>[0-9]+)/$', attestation_inscription, name='etudiant_attestation'),

]

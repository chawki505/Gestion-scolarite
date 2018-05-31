from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^$', dashboard_home_page, name='dashboard_home_page'),

    url(r'^inscriptions/', include('inscriptions.urls')),

    url(r'^modules/', include('modules.urls')),

]

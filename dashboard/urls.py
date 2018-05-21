from django.conf.urls import url

from .views import dashbord_page

urlpatterns = [
    url(r'^$', dashbord_page, name='dashboard_home_page'),
]

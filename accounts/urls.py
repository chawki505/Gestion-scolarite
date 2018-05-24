from django.conf.urls import url, include

from .views import login_account, logout_account, register_account

urlpatterns = [
    url(r'^login/$', login_account, name='login_account'),
    url(r'^logout/$', logout_account, name='logout_account'),
    url(r'^register/$', register_account, name='register_account'),
]

from django.conf.urls import include,url
from django.contrib import admin
from . import views
app_name = 'vip'
urlpatterns = [
    url(r'^', views.vip, name='home'),
    #url(r'^reincio/(?P<id_reinicio>\d+)$/(?P<id_user>\d+)$',views.reinicio, name='reincio')
    url(r'^reincio/(?P<id_reinicio>\d+)',views.reinicio, name='reincio')
]

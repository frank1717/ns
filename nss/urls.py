from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.vip, name='home'),
    url(r'^vip/', views.vip, name='index'),
    #url(r'^reincio/(?P<id_reinicio>\d+)$/(?P<id_user>\d+)$',views.reinicio, name='reincio')
    url(r'^reinicio/(?P<id_reinicio>[0-9A-Za-z_\-]+)/(?P<id_user>[0-9A-Za-z_\-]+)$',views.reinicio,name='reinicio'),
    #[0-9A-Za-z_\-]+)/
]

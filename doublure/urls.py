from django.conf.urls import include, url
from . import views

app_name = 'doublure'

urlpatterns = [url(r'^(?P<id>[0-9]+)/(?P<pk>[0-9]+)/$', views.DoublureDetail, name='doublureDetail'),
               url(r'^confirm/(?P<uuid>\w+)/$', views.ConfirmDoublure, name='confirmation'),
               url(r'^index/$', views.IndexView.as_view(), name='indexstag'),
               url(r'^index/(?P<id>[0-9]+)/$', views.DoublureIndexView, name='indexdoublure'),
               url(r'^(?P<pk>[0-9]+)/edit/(?P<id>[0-9]+)/$', views.DoublureModification, name='modif'),
               url(r'^global/(?P<id>[0-9]+)/$', views.VisionGlobale, name='global'),
               url('tat/',views.Nouvelle,name='nouvelle'),

]

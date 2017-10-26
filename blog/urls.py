from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index' ),
    url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
    url(r'^about/$', views.about, name='about')
]

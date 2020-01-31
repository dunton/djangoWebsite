from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^pictures/', views.pictures, name='pictures'),
    url(r'^resume/', views.resume, name='resume'),
]

urlpatterns += staticfiles_urlpatterns()

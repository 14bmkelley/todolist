from django.conf.urls import patterns, url
from todoapp import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'profile', views.profile, name='profile'),
    url(r'about', views.about, name='about'),
)

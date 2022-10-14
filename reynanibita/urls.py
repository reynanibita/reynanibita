from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('portpolio', views.portpolio, name='portpolio'),
    path('services', views.services, name='services'),
]
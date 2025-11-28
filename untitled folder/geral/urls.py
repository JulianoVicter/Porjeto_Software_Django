from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('inicio/', views.index, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('termos/', views.termos, name='termos'),
]

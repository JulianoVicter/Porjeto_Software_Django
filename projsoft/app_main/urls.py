from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('criar-conta/', views.cria_conta, name='cria_conta'),
    path('criar-conta/', views.criar_conta, name='criar_conta'),

    
]

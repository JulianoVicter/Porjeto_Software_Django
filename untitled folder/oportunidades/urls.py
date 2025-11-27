from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('lista_projetos/', views.lista_projetos, name='lista_projetos'),
    path('filtro/', views.filtro, name='filtro'),
    path('projeto/', views.projeto, name='projeto'),
    path('inscricao/', views.inscricao, name='inscricao'),
]

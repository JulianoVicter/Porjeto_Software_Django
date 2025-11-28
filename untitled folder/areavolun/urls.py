from django.urls import path
from . import views

urlpatterns = [
    path('', views.area, name='area'),
    path('calendario/', views.calendario, name='calendario'),
    path('historico/', views.historico, name='historico'),
    path('aceito/', views.aceito, name='aceito'),
    path('rejeitado/', views.rejeitado, name='rejeitado'),
    path('analise/', views.analise, name='analise'),
]


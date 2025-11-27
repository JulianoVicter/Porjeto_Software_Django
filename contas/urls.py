from django.urls import path
from . import views

urlpatterns = [
    path('', views.escolha_perfil, name='escolha_perfil'),
    path('login/', views.login, name='login'),
    path('login-ong/', views.login_ong, name='login_ong'),
    path('conta/', views.conta, name='conta'),
    path('criar_conta_ong/', views.criar_conta_ong, name='criar_conta_ong'),
    path('escolha_perfil/', views.escolha_perfil, name='escolha_perfil'),

]

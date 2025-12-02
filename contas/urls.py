from django.urls import path

from . import views

urlpatterns = [
    path("", views.escolha_perfil, name="escolha_perfil"),
    path("login/", views.login, name="login"),
    path("login/ong/", views.login, name="login_ong"),
    path("logout/", views.logout, name="logout"),
    path("voluntario/criar/", views.criar_conta_voluntario, name="criar_conta_voluntario"),
    path("organizacao/criar/", views.criar_conta_ong, name="criar_conta_ong"),
    path("voluntario/area/", views.area_voluntario, name="area_voluntario"),
    path("organizacao/dashboard/", views.dashboard_ong, name="dashboard_ong"),
]

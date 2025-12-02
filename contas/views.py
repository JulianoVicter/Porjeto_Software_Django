from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, OrganizacaoSignupForm, VoluntarioSignupForm
from .models import OrganizacaoProfile, VoluntarioProfile


def escolha_perfil(request):
    return render(request, "contas/escolha_perfil.html")


def criar_conta_voluntario(request):
    if request.method == "POST":
        form = VoluntarioSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta de voluntário criada com sucesso! Faça login para continuar.")
            return redirect("contas:login")
    else:
        form = VoluntarioSignupForm()
    return render(request, "contas/conta.html", {"form": form, "titulo": "Criar conta de voluntário"})


def criar_conta_ong(request):
    if request.method == "POST":
        form = OrganizacaoSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta de organização criada com sucesso! Faça login para continuar.")
            return redirect("contas:login")
    else:
        form = OrganizacaoSignupForm()
    return render(request, "contas/criar_conta_ong.html", {"form": form, "titulo": "Criar conta de organização"})


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect(
                    "contas:area_voluntario" if hasattr(user, "perfil_voluntario") else "contas:dashboard_ong"
                )
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = LoginForm(request)
    return render(request, "contas/login.html", {"form": form})


@login_required
def area_voluntario(request):
    perfil = None
    try:
        perfil = request.user.perfil_voluntario
    except VoluntarioProfile.DoesNotExist:
        pass
    return render(request, "contas/area_voluntario.html", {"perfil": perfil})


@login_required
def dashboard_ong(request):
    perfil = None
    try:
        perfil = request.user.perfil_organizacao
    except OrganizacaoProfile.DoesNotExist:
        pass
    return render(request, "contas/dashboard_ong.html", {"perfil": perfil})


def logout(request):
    auth_logout(request)
    messages.info(request, "Sessão encerrada.")
    return redirect("inicio")

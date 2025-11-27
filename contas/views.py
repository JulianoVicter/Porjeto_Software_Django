from django.shortcuts import render

def login(request):
    return render(request, 'contas/login.html')

def conta(request):
    return render(request, 'contas/conta.html')

def escolha_perfil(request):
    return render(request, 'contas/escolha_perfil.html')

def login_ong(request):
    return render(request, 'contas/login_ong.html')

def criar_conta_ong(request):
    return render(request, 'contas/criar_conta_ong.html')


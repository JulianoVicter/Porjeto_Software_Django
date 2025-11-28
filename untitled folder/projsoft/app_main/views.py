from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UsuarioForm, ContatoForm


def index(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso! Entraremos em contato em breve.")
            return redirect('index')
    else:
        form = ContatoForm()

    return render(request, 'app_main/index.html', {'form': form})


def sobre(request):
    return render(request, 'app_main/sobre.html')


def cria_conta(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Você já pode fazer login.")
            return redirect('index')
    else:
        form = UsuarioForm()

    return render(request, 'app_main/criaConta.html')

def criar_conta(request):
    return render(request, 'app_main/criaConta.html')

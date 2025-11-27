from django.shortcuts import render

def lista_projetos(request):
    return render(request, 'oportunidades/lista_projetos.html')

def projeto(request):
    return render(request, 'oportunidades/projeto.html')

def inscricao(request):
    return render(request, 'oportunidades/inscricao.html')

def filtro(request):
    return render(request, 'oportunidades/filtro.html')

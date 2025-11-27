from django.shortcuts import render

def index(request):
    return render(request, 'geral/index.html')

def sobre(request):
    return render(request, 'geral/sobre.html')

def termos(request):
    return render(request, 'geral/termos.html')

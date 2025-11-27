from django.shortcuts import render

def dashboard(request):
    return render(request, 'ong/dashboard.html')

def inscritos(request):
    return render(request, 'ong/inscritos.html')
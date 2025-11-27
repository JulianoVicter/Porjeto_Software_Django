from django.shortcuts import render

def area(request):
    return render(request, 'areavolun/area.html')

def calendario(request):
    return render(request, 'areavolun/calendario.html')

def historico(request):
    return render(request, 'areavolun/historico.html')

def aceito(request):
    return render(request, 'areavolun/aceito.html')

def rejeitado(request):
    return render(request, 'areavolun/rejeitado.html')

def analise(request):
    return render(request, 'areavolun/analise.html')



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('geral.urls')),
    path('admin/', admin.site.urls),
    path('contas/', include(('contas.urls', 'contas'), namespace='contas')),
    path('oportunidades/', include('oportunidades.urls')),
    path('areavolun/', include('areavolun.urls')),
    path('area/', include('areavolun.urls')),
    path('ong/', include('ong.urls')),




]

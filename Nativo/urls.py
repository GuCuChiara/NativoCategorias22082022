"""Nativo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aplicaciones.principal import views
from Aplicaciones.principal.views import inicio, busqueda_diagnosticos, buscar_CIE10, autocomplete, autocomplete3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name='index'),# en index no va nada entre ''
    path('buscar/', views.buscar, name ='buscar'),
    path('busqueda_dx/', views.busqueda_diagnosticos, name='busqueda_dx'), #busqueda_prestaciones
    path('buscar_CIE10/', views.buscar_CIE10, name ='buscar_CIE10'),
    path('buscar_CIE10_x/', views.buscar_CIE10_x, name ='buscar_CIE10_x'),
    path('autocomplete2/', views.autocomplete, name ='autocomplete2'),
    path('autocomplete3/', views.autocomplete3, name ='autocomplete3'),
    path('buscar_AMS/', views.buscar_AMS, name ='buscar_AMS')
]

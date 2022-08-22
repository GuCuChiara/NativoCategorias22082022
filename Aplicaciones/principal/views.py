from multiprocessing import context
from django.shortcuts import render
from .models import cie10nativo, codigossancor, prestaxcie10
from .forms import AMSForm, CIE10Form, CIE10xForm
import json

from django.http import JsonResponse
# Create your views here. VISTA
#archivo index.html: reemplaza el inicio por defecto de Django:
def inicio(request):
    return render(request, "index.html")

def busqueda_diagnosticos(request): #name='busqueda_dx'
    prestaciones = codigossancor.objects.all
    diagnosticosCIE10 = cie10nativo.objects.all
    #el condicional de abajo es por si se usa autocomplete
    if 'term' in request.GET:
        qs = cie10nativo.objects.filter(CIE10_DESC__icontains =request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.CIE10_DESC)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    ###
    elif 'term' in request.GET:
        qs2 = codigossancor.objects.filter(Presta_Id__icontains =request.GET.get('term'))
        titles2 = list()
        for product in qs2:
            titles2.append(product.Presta_Id)
        # titles = [product.title for product in qs]
        return JsonResponse(titles2, safe=False)
    ### fin condicional si se usa autocomplete
    return render(request, 
        "busqueda_dx.html", 
        {"showprestaciones":prestaciones,
        "showCIE10": diagnosticosCIE10},
        ) #renderizamos la url busqueda_dx.HTML

# POSICIÓN 1 EN busqueda_dx.HTML--> resultados_busqueda.html
def buscar(request):
    if request.GET ["diag"]:
        #mensaje="Diagnóstico buscado: %r" %request.GET["diag"]
        producto=request.GET ["diag"]
        #Diagnósticos CIE 10 según prestación relacionada en tabla prestaxcie10:
        # variable codigo, se busca en cie10nativo el código CIE 10 vinculado a la prestación AMS buscada (producto)
        # from cie10nativo WHERE producto In prestaxcie10 = (prestacion_Id <--> codCIE10_Id)  
        codigo= cie10nativo.objects.filter(codigossancors__Presta_Id__icontains = producto).order_by('id', 'CIE_10_Id').values() 
        prod=codigossancor.objects.filter (Presta_Id__icontains = producto)
        # contexto:     "producto" = lo buscado
        #               "codigo" = codigo, búsqueda en cie10nativo
        #               "query": = prod, búsqueda en codigossancor
        context={"codigo":codigo, "query":prod, "producto":producto}
        return render(request, "resultados_busqueda.html", context)
        #importante arriba que estén escrito igual!!!! "codigo":codigo,
    else:
        #mensaje="Debes escribir algo!"
        return render(request, "error.html")  

# POSICIÓN 2 EN busqueda_dx.HTML--> resultados_busqueda.html
def buscar_AMS(request):			
    if request.GET ["diag4"]:
        producto=request.GET ["diag4"]
        # variable codigo busca en codigossancor, la prestación AMS vinculada al término ingresado (producto)
        # from codigossancor WHERE producto In codigossancor = (Presta_Id <--> Descripcion)  
        codigo= codigossancor.objects.filter(Descripcion__icontains = producto)
        #nuevo
        #buscamos los códigos CIE10 vinculados y excluímos los resultados que contengan 'Otras'
        codigo2= cie10nativo.objects.filter(codigossancors__Descripcion__icontains=producto).order_by('id','CIE_10_Id').values()
        #nuevo 
        return render(request, "resultados_busqueda4.html", {
            "codigo":codigo, 
            "query":producto, 
            "codigo2":codigo2
            })
    else:
        #mensaje="Debes escribir algo!"
        return render(request, "error.html")    

# POSICIÓN 3 EN busqueda_dx.HTML --> resultados_busqueda2.html
def buscar_CIE10(request): 
    if request.GET ["diag2"]:
        producto=request.GET ["diag2"]
        # variable cod busca en codigossancor la prestación AMS vinculada al código CIE 10 buscado (producto)
        # from codigossancor WHERE producto In prestaxcie10 = (codCIE10_Id <--> prestacion_Id)  
        cod=codigossancor.objects.filter(cie10nativos__CIE_10_Id__icontains=producto).distinct() #.distinct (eliminamos registros de prestaciones duplicados)
        #variable prod busca en cie10nativo el código CIE 10 buscado = producto
        prod=cie10nativo.objects.filter(CIE_10_Id__icontains=producto).order_by('id', 'CIE_10_Id').values()
        # contexto:     "producto" = lo buscado
        #               "codigo" = cod, búsqueda en códigossancor
        #               "query": = prod, búsqueda en cie10nativo
        context={"codigo":cod, "query":prod, "producto":producto}
        return render(request, "resultados_busqueda2.html", context)
    else:
        #mensaje="Debes escribir algo!"
        return render(request, "error.html")

# POSICIÓN 4 EN busqueda_dx.HTML --> resultados_busqueda3.html
def buscar_CIE10_x(request):
    if request.GET ["diag3"]:
        producto=request.GET ["diag3"]
        # variable codigo busca en cie10nativo el código CIE 10 vinculado al diagnóstico CIE 10 buscado (producto)
        # from cie10nativo WHERE producto In cie10nativo = (CIE_10_Id <--> CIE10_DESC)  
        #----------------------------------------------------------------------------------------
        #   para ordenar según score del id en forma jerárquica
        #   codigo= cie10nativo.objects.filter(CIE10_DESC__icontains = producto).order_by('id').values() 
        #----------------------------------------------------------------------------------------
        codigo= cie10nativo.objects.filter(CIE10_DESC__icontains = producto).order_by('id','CIE_10_Id').values()
        cod=codigossancor.objects.filter(cie10nativos__CIE10_DESC__icontains=producto).distinct() #.distinct (eliminamos registros de prestaciones duplicados)
        # contexto: {} al final del request      "codigo" = codigo, búsqueda en cie10nativo
        #                                        "query": = producto, = lo buscado
        return render(request, "resultados_busqueda3.html", {
            "codigo":codigo, 
            "query":producto,
            "cod":cod})
    else:
        #mensaje="Debes escribir algo!"
        return render(request, "error.html")      

def autocomplete (request):
    if 'term' in request.GET:
        qs = cie10nativo.objects.filter(CIE10_DESC__icontains =request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.CIE10_DESC)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, "autocomplete2.html")      

def autocomplete3 (request):
    if 'term' in request.GET:
        qs2 = codigossancor.objects.filter(Presta_Id__icontains =request.GET.get('term'))
        titles2 = list()
        for product in qs2:
            titles2.append(product.Presta_Id)
        # titles = [product.title for product in qs]
        return JsonResponse(titles2, safe=False)
    return render(request, "autocomplete3.html")      
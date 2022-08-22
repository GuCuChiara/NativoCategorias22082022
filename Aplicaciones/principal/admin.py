from re import search
from django.contrib import admin
from .models import cie10nativo, codigossancor, prestaxcie10
# Register your models here.
class Diagno_Mostrar(admin.ModelAdmin):
    list_display=("CIE_10_Id", "CIE10_DESC")
    search_fields=("CIE_10_Id", "CIE10_DESC")
    #list_filter=("CIE_10_Id",) #campo de búsqueda filtrada
    #"CIE_10_Id", "CIE10_DESC"

class Cod_Mostrar(admin.ModelAdmin):
    list_display=("Presta_Id", "Descripcion")
    search_fields=("Presta_Id", "Descripcion")
    #list_filter=("CIE_10",) #campo de búsqueda filtrada
    #"Presta_Id", "Descripcion"

class Mix_Mostrar(admin.ModelAdmin):
    list_display=("prestacion_Id", "codCIE10_Id")
    search_fields=("prestacion_Id", "codCIE10_Id") #!!!! NO FUNCIONA!!!!
    #list_filter=("Presta_Id", "CIE_10_Id",) #campo de búsqueda filtrada

admin.site.register(cie10nativo, Diagno_Mostrar)
admin.site.register(codigossancor, Cod_Mostrar)
admin.site.register(prestaxcie10, Mix_Mostrar)

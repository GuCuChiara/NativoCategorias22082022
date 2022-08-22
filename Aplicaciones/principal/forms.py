from dataclasses import fields

from django import forms
from .models import codigossancor, cie10nativo, prestaxcie10

#creamos con Django un formulario html basado en el modelo Diagnostico
class AMSForm(forms.ModelForm):
    class Meta:
        model = codigossancor
        fields = '__all__' #todos los campos, se puede personalizar
        #fields =('SNOMED_CT_ID', 'SNOMED_CT_FSN', ) # se puede personalizar (coma al final, es una tupla)

class CIE10Form(forms.ModelForm):
    class Meta:
        model = cie10nativo
        fields = '__all__' #todos los campos, se puede personalizar

class CIE10xForm(forms.ModelForm):
    class Meta:
        model = prestaxcie10
        fields = '__all__' #todos los campos, se puede personalizar
# importarlo dps en views! 
# from .forms import codigossancor
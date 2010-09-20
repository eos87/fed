from django import forms
from django.forms import ModelForm
import datetime

from fed.encuesta.models import *

class InfluenciaForm(forms.Form):
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all(), label='Organizaciones')#, widget=forms.CheckboxSelectMultiple)
    resultado = forms.ModelMultipleChoiceField(queryset=Resultado.objects.all(), label='Resultados')
    desde = forms.DateField(label='Desde')
    hasta = forms.DateField(label='Hasta')



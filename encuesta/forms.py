# -*- coding: UTF-8 -*-

from django import forms
from django.forms import ModelForm
import datetime

from fed.encuesta.models import *

class InfluenciaForm(forms.Form):
    tipo = forms.MultipleChoiceField(choices=TIPO_CHOICE, label='Modalidad de apoyo')
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all(), label='Organizaciones')#, widget=forms.CheckboxSelectMultiple)
    resultado = forms.ModelMultipleChoiceField(queryset=Resultado.objects.all(), label='Resultados')
    periodo = forms.MultipleChoiceField(choices=CHOICE_PERIODO, label='Período')
    anio = forms.ChoiceField(choices=CHOICE_ANIO, label='Año')

class IndicadoresForm(forms.Form):
    tipo = forms.MultipleChoiceField(choices=TIPO_CHOICE, label='Modalidad de apoyo')
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all(), label='Organizaciones')#, widget=forms.CheckboxSelectMultiple)
    #municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all(), label='Municipios')
    periodo = forms.MultipleChoiceField(choices=CHOICE_PERIODO, label='Período')
    anio = forms.ChoiceField(choices=CHOICE_ANIO, label='Año')



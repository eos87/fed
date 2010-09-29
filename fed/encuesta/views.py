from decorators import session_required
from django.core.exceptions import ViewDoesNotExist
from django.db.models import Sum
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from forms import *
from models import *

import json

def _queryset_filtrado(request, resultado):
    '''metodo para obtener el queryset de encuesta
    segun los filtros del formulario que son pasados
    por la variable de sesion'''
    rt = ResultadoTrabajado.objects.filter(resultado=resultado, municipio__in=request.session['municipio'])    
    list = []
    for r in rt:
        if request.session['desde'] <= r.encuesta.fecha_inicio <= request.session['hasta']:
            list.append(r.encuesta.id)
    return Encuesta.objects.filter(pk__in=list)
    

def index(request):
    return direct_to_template(request, 'index.html')

def influencia(request):
    if request.is_ajax():
        form = InfluenciaForm(request.POST)
        if form.is_valid():
            lista = []
            dicc = {}
            resultados = []
            bandera = 1            
            encuestas = Encuesta.objects.filter(organizacion__in=form.cleaned_data['organizacion'], periodo__in=form.cleaned_data['periodo'], anio=form.cleaned_data['anio'])
            for encuesta in encuestas:
                for resultado in encuesta.resultadotrabajado_set.filter(resultado__in=form.cleaned_data['resultado']):
                    for muni in resultado.municipio.all():
                        lista.append(muni)
            munis = set(lista)
            for municipio in munis:
                #consultar los proyectos de estos municipios
                rts = municipio.resultadotrabajado_set.filter(resultado__in=form.cleaned_data['resultado'])
                #rts = ResultadoTrabajado.objects.filter(resultado__in=form.cleaned_data['resultado'], municipio=municipio)
                proys = []
                for r in rts:
                    if r.encuesta.organizacion in form.cleaned_data['organizacion']:
                        proys.append(r.encuesta.proyecto.pk)
                proyectos = Proyecto.objects.filter(id__in=proys).values('id', 'nombre')

                dicc = {
                    'punto': (float(municipio.latitud), float(municipio.longitud)),
                    'municipio': municipio.nombre,
                    'proyectos': list(proyectos)
                }

            resultados.append(dicc)           
            if not encuestas:
                bandera = 0

            return HttpResponse(json.dumps(resultados).replace('"', '\\"'), mimetype='application/json')
    else:
        form = InfluenciaForm()
        bandera = 0

    return render_to_response('fed/influencia.html', RequestContext(request, locals()))

def indicadores(request):
    if request.method == 'POST':
        form = IndicadoresForm(request.POST)
        if form.is_valid():
            bandera = 1
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['desde'] = form.cleaned_data['desde']
            request.session['hasta'] = form.cleaned_data['hasta']
            request.session['activo'] = True
            resultados = Resultado.objects.all()
    else:
        form = IndicadoresForm()
        bandera = 0
    return render_to_response('fed/indicadores.html', RequestContext(request, locals()))

def resultado1(request):
    bandera = 11;
    resultado = Resultado.objects.get(pk=1)
    return render_to_response('fed/res/resultado1.html', RequestContext(request, locals()))

#vistas para indicadores, no hay forma de volverlos dinamicos
@session_required
def indicador111(request):
    resultado = Resultado.objects.get(pk=1)
    tabla = {}
    tabla2 = {}
    tabla3 = {}
    a = _queryset_filtrado(request, resultado)
    for opcion in CHOICE_MEDIO:
        query = AccionEfectuadaMedio.objects.filter(encuesta__in=a, accion=opcion[0])
        cantidad_sum = query.aggregate(cantidad_sum=Sum('cantidad'))['cantidad_sum']
        participantes_sum = query.aggregate(participantes_sum=Sum('participantes'))['participantes_sum']
        tabla[opcion[1]] = {'cantidad':cantidad_sum, 'participantes': participantes_sum}


    for opcion in CHOICE_REGION:
        query = AccionEfectuadaRegion.objects.filter(encuesta__in=a, accion=opcion[0])
        cantidad_sum = query.aggregate(cantidad_sum=Sum('cantidad'))['cantidad_sum']
        participantes_sum = query.aggregate(participantes_sum=Sum('participantes'))['participantes_sum']

        tabla2[opcion[1]] = {'cantidad':cantidad_sum, 'participantes': participantes_sum}

    for opcion in CHOICE_DOCS:
        query = AccionEfectuadaDocumento.objects.filter(encuesta__in=a, accion=opcion[0])
        cantidad_sum = query.aggregate(cantidad_sum=Sum('cantidad'))['cantidad_sum']
        participantes_sum = query.aggregate(participantes_sum=Sum('participantes'))['participantes_sum']
        prom = get_prom(cantidad_sum, participantes_sum)

        tabla3[opcion[1]] = {'cantidad':cantidad_sum, 'participantes': participantes_sum, 'prom':prom}

    return render_to_response('fed/indicador111.html', RequestContext(request, locals()))

@session_required
def indicador112(request):
    resultado = Resultado.objects.get(pk=1)
    tabla = {}
    a = _queryset_filtrado(request, resultado)

    for opcion in CHOICE_REGION:
        query = ParticipacionComisionDecision.objects.filter(encuesta__in=a, accion=opcion[0])
        instancias_sum = query.aggregate(instancias_sum=Sum('cantidad_instancias'))['instancias_sum']
        acciones_promovidas_sum = query.aggregate(acciones_promovidas_sum=Sum('cantidad_acciones_promovidas'))['acciones_promovidas_sum']
        acciones_efectivas_sum = query.aggregate(acciones_efectivas_sum=Sum('cantidad_acciones_efectivas'))['acciones_efectivas_sum']
        prom = get_prom(acciones_promovidas_sum, acciones_efectivas_sum)

        tabla[opcion[1]] = {
            'instancias':instancias_sum,
            'acciones_promovidas': acciones_promovidas_sum,
            'acciones_efectivas': acciones_efectivas_sum,
            'prom':prom
            }

    return render_to_response('fed/indicador112.html', RequestContext(request, locals()))

@session_required
def indicador113(request):
    resultado = Resultado.objects.get(pk=1)
    tabla = {}
    a = _queryset_filtrado(request, resultado)
    
    for opcion in CHOICE_REGION:
        query = ParticipacionComisionAgenda.objects.filter(encuesta__in=a, accion=opcion[0])
        instancias_sum = query.aggregate(instancias_sum=Sum('cantidad_instancias'))['instancias_sum']
        acciones_promovidas_sum = query.aggregate(acciones_promovidas_sum=Sum('cantidad_acciones_prom'))['acciones_promovidas_sum']
        acciones_efectivas_sum = query.aggregate(acciones_efectivas_sum=Sum('cantidad_acciones_efec'))['acciones_efectivas_sum']
        prom = get_prom(acciones_promovidas_sum, acciones_efectivas_sum)

        tabla[opcion[1]] = {
            'instancias':instancias_sum,
            'acciones_promovidas': acciones_promovidas_sum,
            'acciones_efectivas': acciones_efectivas_sum,
            'prom':prom
            }

    return render_to_response('fed/indicador113.html', RequestContext(request, locals()))

@session_required
def indicador114(request):
    resultado = Resultado.objects.get(pk=1)
    tabla = {}
    a = _queryset_filtrado(request, resultado)

    '''if len(a)==0:
        return HttpResponse('No hay datos', mimetype='text/plain')'''

    for opcion in CHOICE_REGION:
        query = AccionObservatorio.objects.filter(encuesta__in=a, accion=opcion[0])
        observatorio_sum = query.aggregate(observatorio_sum=Sum('cantidad_observatorios'))['observatorio_sum']
        acciones_realizadas_sum = query.aggregate(acciones_realizadas_sum=Sum('cantidad_acciones_realiz'))['acciones_realizadas_sum']
        acciones_web_sum = query.aggregate(acciones_web_sum=Sum('cantidad_acciones_web'))['acciones_web_sum']
        prom = get_prom(acciones_realizadas_sum, acciones_web_sum)

        tabla[opcion[1]] = {
            'observatorio':observatorio_sum,
            'acciones_realizadas': acciones_realizadas_sum,
            'acciones_web': acciones_web_sum,
            'prom':prom
            }

    return render_to_response('fed/indicador114.html', RequestContext(request, locals()))

def resultado2(request):
    bandera = 11;
    resultado = Resultado.objects.get(pk=2)
    return render_to_response('fed/res/resultado1.html', RequestContext(request, locals()))

@session_required
def indicador121(request):
    resultado = Resultado.objects.get(pk=2)
    tabla = {}
    tabla2 = {}
    tabla3 = {}
    a = _queryset_filtrado(request, resultado)

    for opcion in CHOICE_MEDIO:
        #calculando denuncias realizadas
        query = DenunciaSocialRealizada.objects.filter(encuesta__in=a, accion=opcion[0])
        div_sexual_sum = query.aggregate(div_sexual_sum=Sum('persona_div_sexual'))['div_sexual_sum']
        discapacidad_sum = query.aggregate(discapacidad_sum=Sum('persona_discapacidad'))['discapacidad_sum']
        vih_sum = query.aggregate(vih_sum=Sum('persona_vih'))['vih_sum']
        racial_sum = query.aggregate(racial_sum=Sum('persona_racial'))['racial_sum']
        joven_sum = query.aggregate(joven_sum=Sum('persona_joven'))['joven_sum']

        tabla[opcion[1]] = {
            'sexual':div_sexual_sum,
            'discapacidad': discapacidad_sum,
            'vih': vih_sum,
            'racial': racial_sum,
            'joven':joven_sum
            }

        #calculando denuncias efectivas
        query2 = DenunciaSocialEfectiva.objects.filter(encuesta__in=a, accion=opcion[0])
        div_sexual_sum2 = query2.aggregate(div_sexual_sum2=Sum('persona_div_sexual'))['div_sexual_sum2']
        discapacidad_sum2 = query2.aggregate(discapacidad_sum2=Sum('persona_discapacidad'))['discapacidad_sum2']
        vih_sum2 = query2.aggregate(vih_sum2=Sum('persona_vih'))['vih_sum2']
        racial_sum2 = query2.aggregate(racial_sum2=Sum('persona_racial'))['racial_sum2']
        joven_sum2 = query2.aggregate(joven_sum2=Sum('persona_joven'))['joven_sum2']

        tabla2[opcion[1]] = {
            'sexual':div_sexual_sum2,
            'discapacidad': discapacidad_sum2,
            'vih': vih_sum2,
            'racial': racial_sum2,
            'joven':joven_sum2
            }

        #calculando promedios
        div_sexual_prom = get_prom(div_sexual_sum, div_sexual_sum2)
        discapacidad_prom = get_prom(discapacidad_sum, discapacidad_sum2)
        vih_prom = get_prom(vih_sum, vih_sum2)
        racial_prom = get_prom(racial_sum, racial_sum2)
        joven_prom = get_prom(joven_sum, joven_sum2)

        tabla3[opcion[1]] = {
            'sexual':div_sexual_prom,
            'discapacidad': discapacidad_prom,
            'vih': vih_prom,
            'racial': racial_prom,
            'joven':joven_prom
            }

    return render_to_response('fed/indicador121.html', RequestContext(request, locals()))

#obtener la vista adecuada para los indicadores
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    '1': resultado1,
    '2': resultado2,

    #inicia vistas de indicadores
    'indicador-111': indicador111,
    'indicador-112': indicador112,
    'indicador-113': indicador113,
    'indicador-114': indicador114,
    #indicadores para resultado 1.2
    'indicador-121': indicador121,
    }

def get_prom(total, cantidad):
    x = (cantidad * 100) / float(total)
    return x
from django.core.exceptions import ViewDoesNotExist
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from decorators import session_required
from forms import *
from models import *

def _queryset_filtrado(request):
    '''metodo para obtener el queryset de encuesta
    segun los filtros del formulario que son pasados
    por la variable de sesion'''
    params = {}
    if request.session['organizacion']:
        params['organizacion__in'] = request.session['organizacion']
    if request.session['municipio']:
        proyectos = Proyecto.objects.filter(organizacion__in=request.session['organizacion'], municipio__in=request.session['municipio'])
        params['proyecto__in'] = proyectos
    if request.session['desde'] and request.session['hasta']:
        params['fecha_inicio__range'] = (request.session['desde'], request.session['hasta'])

    return Encuesta.objects.filter(**params)

def index(request):
    return direct_to_template(request, 'index.html')

def influencia(request):
    if request.method == 'POST':
        form = InfluenciaForm(request.POST)
        if form.is_valid():
            lista = []
            municipios = {}
            bandera = 1            
            encuestas = Encuesta.objects.filter(organizacion__in=form.cleaned_data['organizacion'], fecha_inicio__range=(form.cleaned_data['desde'], form.cleaned_data['hasta']))            
            for encuesta in encuestas:
                for resultado in encuesta.resultadotrabajado_set.filter(resultado__in=form.cleaned_data['resultado']):
                    for muni in resultado.municipio.all():
                        lista.append(muni)
            munis = set(lista)
            for municipio in munis:
                municipios[municipio] = []
                #consultar los proyectos de estos municipios
                rts = municipio.resultadotrabajado_set.filter(resultado__in=form.cleaned_data['resultado'])
                #rts = ResultadoTrabajado.objects.filter(resultado__in=form.cleaned_data['resultado'], municipio=municipio)
                for r in rts:
                    if r.encuesta.organizacion in form.cleaned_data['organizacion']:
                        municipios[municipio].append(r.encuesta.proyecto.descripcion)
            
            if not encuestas:
                bandera = 0
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
    a = _queryset_filtrado(request)
    for opcion in CHOICE_MEDIO:
        query = a.accionefectuadamedio_set.filter(accion=opcion[0])

    return render_to_response('fed/indicador111.html', RequestContext(request, locals()))

#obtener la vista adecuada para los indicadores
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    '1': resultado1,

    #inicia vistas de indicadores
    'indicador-111': indicador111,
    }

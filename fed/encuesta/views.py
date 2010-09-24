from decorators import session_required
from django.core.exceptions import ViewDoesNotExist
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from forms import *
from models import *

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

#obtener la vista adecuada para los indicadores
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    '1': resultado1,

    #inicia vistas de indicadores
    'indicador-111': indicador111,
    'indicador-112': indicador112,
    'indicador-113': indicador113,
    }

def get_prom(total, cantidad):
    x = (cantidad * 100) / total
    return x
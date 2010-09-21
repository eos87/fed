from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.shortcuts import render_to_response

from forms import *

def _queryset_influencia(request):
    '''metodo para obtener el queryset de encuesta
    segun los filtros del formulario que son pasados
    por la variable de sesion'''


def index(request):
    return direct_to_template(request, 'index.html')

def influencia(request):
    #dict = {'form': form,'user': request.user,'centinela':centinela}
    if request.method == 'POST':
        form = InfluenciaForm(request.POST)
        if form.is_valid():
            munis = []
            municipios = {}
            bandera = 1            
            encuestas = Encuesta.objects.filter(organizacion__in=form.cleaned_data['organizacion'], fecha_inicio__range=(form.cleaned_data['desde'], form.cleaned_data['hasta']))            
            for encuesta in encuestas:
                for resultado in encuesta.resultadotrabajado_set.filter(resultado__in=form.cleaned_data['resultado']):
                    for muni in resultado.municipio.all():
                        if not muni in munis:
                            munis.append(muni)

            #for municipio in munis:
            #    municipios[municipio] = []
            
            if not encuestas:
                bandera = 0
    else:
        form = InfluenciaForm()
        bandera = 0

    return render_to_response('fed/influencia.html', RequestContext(request, locals()))

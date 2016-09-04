from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView

from .models import Chc
from .models import Turnos
from .models import Dres
from .models import Espec

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def validar_ingreso(request):
	if request.method == 'POST':
                formvar = request.POST
                documentovalue = str(formvar['documento'])
                telefonovalue = str(formvar['telefono'])
        chc_info = Chc.objects.all().filter(nro_doc = documentovalue)
        chc_info = chc_info.filter(tele = telefonovalue)
        dicmedicos = {}
        context = locals()

        if not chc_info:
                print "NOvalido"
                mensaje = "Paciente NO registrado o Clave Incorrecta."
                mensaje2 = "Solicite turno telefonicamente."
                context['MENSAJE'] = mensaje
                context['MENSAJE2'] = mensaje2
                return render(request, 'turnosapp/novalidaingreso.html', context)

	return True

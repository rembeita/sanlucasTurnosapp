# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView

from .models import Chc
from .models import Turnos
from .models import Dres
from .models import Espec
from .models import Tblhmed

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

#from inicio import *

def index(request):
	context = locals()
	flag = False

# Ejemp,o
#	chc_info = Chc.objects.all().filter(nro_doc = dniPaciente)
#	idpaciente = str(chc_info.values("id")[0]["id"])
#	print "##### " + str(idpaciente)
#	relacion_paciente = PacienteTurnoMedico.objects.all().filter(is_active = 1).filter(chc_id = idpaciente)
#
	if (flag == True):
		return render(request, 'turnosapp/mantenimiento.html', context)

	return render(request, 'turnosapp/index.html', context)


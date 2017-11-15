# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db import connection
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView
from .models import Chc
from .models import Turnos
from .models import Turnosdel
from .models import Dres
from .models import Espec
from .models import PacienteTurnoMedico
from .models import Tblhmed
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
import time


def formatear_id_medico(idmedico):
	resultado = 4 - len(idmedico)
	return (" " * resultado) + idmedico

def validaringreso(request):
	if request.method == 'POST':
		formvar = request.POST
		#Si apreto el boton eliminar busco las tablas y las elimino
		if (formvar.has_key('datosturnos')):
			datos_turnos = str(formvar['datosturnos'])
			hora_eliminar, id_relacion = datos_turnos.split("||")
			hora_eliminar = hora_eliminar.replace(":","")

			#Comento las lineas para que grabe el sistema sin modificar la hora.
#			if (int(hora_eliminar) < 1000):
#				hora_eliminar = hora_eliminar[1:]
#				hora_eliminar = hora_eliminar[1:]
			hora_eliminar = "T"+hora_eliminar
		        actualizar_turno = PacienteTurnoMedico.objects.get(pk=id_relacion)
			#actualizar_turno.is_active = False
			#print actualizar_turno.turnos_id
			elimt = Turnos.objects.get(id=actualizar_turno.turnos_id)
			ultimo_id_turnosdel = Turnosdel.objects.latest('id').id +1
			print "LALALALA"
			print ultimo_id_turnosdel
			#print "##ULT" + ultimo_id_turnosdel
		 	agregar_turnosdel = Turnosdel(id = ultimo_id_turnosdel, nro_doc = elimt.nro_doc, cod_esp = elimt.cod_esp, dia_tur = elimt.dia_tur, \
						hora_tur = elimt.hora_tur, dhm_tur = elimt.dhm_tur, id_chc = elimt.id_chc, \
						o_social = elimt.o_social, nro_afil = elimt.nro_afil, tipo_doc = elimt.tipo_doc, \
						no_doc = elimt.no_doc, consult = elimt.consult, frec = elimt.frec, usuario = elimt.usuario,\
						ws = elimt.ws, importe = elimt.importe, tel_tur = elimt.tel_tur, plan = elimt.plan, \
						fecalta = elimt.fecalta, horalta = elimt.horalta, coseg = elimt.coseg, \
						usu_modi = elimt.usu_modi, ws_modi = elimt.ws_modi, dia_modi = elimt.dia_modi, \
						hs_modi = elimt.hs_modi, insertado = elimt.insertado, gravado = elimt.gravado)
		        agregar_turnosdel.save()
			print "GRAEEEE" + str(actualizar_turno.tblhmed_id)
			cursor = connection.cursor()
			print ("update tblhmed set "+ hora_eliminar + " = \"X\" where id = " + str(actualizar_turno.tblhmed_id))
			cursor.execute("update tblhmed set "+ hora_eliminar + " = \"X\" where id = " + str(actualizar_turno.tblhmed_id))
			actualizar_turno.delete()
			elimt.delete()

		formvar = request.POST
		documentovalue = str(formvar['documento'])
		telefonovalue = str(formvar['telefono'])
	chc_info = Chc.objects.all().filter(nro_doc = documentovalue)
	chc_info = chc_info.filter(tele__contains = telefonovalue)
	dicmedicos = {}
	context = locals()

	if not chc_info:
		print "NOvalido"
		mensaje = "Paciente NO registrado o Clave Incorrecta."
		mensaje2 = "Solicite turno telefonicamente."
		context['MENSAJE'] = mensaje
		context['MENSAJE2'] = mensaje2
		return render(request, 'turnosapp/novalidaingreso.html', context)


	nombrepaciente = str(chc_info.values("acciden")[0]["acciden"])
	idpaciente = str(chc_info.values("id")[0]["id"])
	dnipaciente = str(chc_info.values("nro_doc")[0]["nro_doc"])
	context['PACIENTE'] = nombrepaciente
	context['DNIPACIENTE'] = dnipaciente
	context['TELEFONO'] = telefonovalue
	context['DOCUMENTO'] = documentovalue
	
	turnos_info = Turnos.objects.all().filter(id_chc = idpaciente)
	sqlmedicos = turnos_info.values("nro_doc")
	sqlespec = turnos_info.values("cod_esp")
		
	medicosxpaciente = []
#	medicosxpaciente2 = {}
	for i in sqlmedicos:
		medicosxpaciente.append(i["nro_doc"])
#		print i
#		medicosxpaciente2[i["nro_doc"]] = i["cod_esp"]
	dicmedicotmp = {}
	
#	print medicosxpaciente
#	print sqlmedicos
#	print sqlespec
	cont=0 
#	for key,value in sqlmedicos.iteritems():
	for i in medicosxpaciente:
		try:
			medicotmp = []
			valor = formatear_id_medico(i)
			#print "VALOR: " + str(valor)
			print(valor) 
			#doctores_info = Dres.objects.all().filter(cod_med = str(valor)).exclude(tex4 = 'N')
			doctores_info = Dres.objects.all().filter(cod_med = str(valor))
			#print "########DOCTORES INFO: " + str(doctores_info.values("nombre")[0]) 
			print "########DOCTORES INFO: " + str(doctores_info.values("nombre")[0]) 
			print "########DOCTORES INFO: " + str(doctores_info.values("tex4")[0]) 
			#Verifico si tiene una N en el campo tex4 y si es el caso lo exceptuo
			if (str(doctores_info.values("tex4")[0]["tex4"]) == "N"):
				cont += 1
				continue
			medicotmp.append(valor)
			#print "###### DOCTORES VALUE: " + str(doctores_info.values("nombre")[0]["nombre"]) 
			medicotmp.append(str(doctores_info.values("nombre")[0]["nombre"]))
			valoresp = str(sqlespec[cont]['cod_esp'])

			#print "###### VALOR ESP: " + valoresp 
			medicotmp.append(str(valoresp))
			valor_esp = formatear_id_medico(valoresp)
			obtener_especialidad = Espec.objects.all().filter(cod_esp = valor_esp).values("nom_esp")[0]["nom_esp"]
			#print "#### ESPEC: " + str(obtener_especialidad)
			medicotmp.append(str(obtener_especialidad))
			medicotmp.append(str(valor_esp))
			dicmedicotmp[valor]= medicotmp
			cont += 1
		except ValueError:
			cont += 1
			print ValueError
			pass
#	print dicmedicotmp
	# Armo diccionario para mostrar en la vista con los turnos ya tomados.
#	print "########" + idpaciente
	relacion_paciente = PacienteTurnoMedico.objects.all().filter(is_active = 1).filter(chc_id = idpaciente)
	lista_diccionario_turnos = []
	turnos_tomados = {}
	today = datetime.now()
	today = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
	for i in relacion_paciente.values():
		turnos_tomados['id_relacion'] = i['auto_increment_id']
		#obtengo dia y hora
		obtener_datos_turnos = Turnos.objects.all().filter(id = i['turnos_id'])
		turnos_tomados['hora'] = obtener_datos_turnos.values("hora_tur")[0]["hora_tur"]
		turnos_tomados['dia'] = obtener_datos_turnos.values("dia_tur")[0]["dia_tur"]
		#Si la fecha del turno es igual a hoy no muestro
		fecha1 = time.strptime(today, "%Y-%m-%d")
		fecha2 = time.strptime(str(turnos_tomados['dia']), "%Y-%m-%d")
		if ( fecha1 >= fecha2 ):
			continue
		#obtengo el nombre del medico
		numero_doctor = obtener_datos_turnos.values("nro_doc")[0]["nro_doc"]
		numero_doctor = formatear_id_medico(numero_doctor)
		obtener_datos_medico = Dres.objects.all().filter(cod_med = numero_doctor)
		turnos_tomados['nom_medico'] = obtener_datos_medico.values("nombre")[0]["nombre"]
		
		#obtengo la especialidad
		valor_esp = formatear_id_medico(str(obtener_datos_turnos.values("cod_esp")[0]["cod_esp"]))
		turnos_tomados["especialidad"] = Espec.objects.all().filter(cod_esp = valor_esp).values("nom_esp")[0]["nom_esp"]
		lista_diccionario_turnos.append(turnos_tomados.copy())


	
	if not dicmedicotmp:
		print "NOvalido DICIONARIO"
		mensaje = "No se encontraron medicos registrados." 
		mensaje2 = "Solicite turno telefonicamente."
		context['MENSAJE'] = mensaje
		context['MENSAJE2'] = mensaje2
		return render(request, 'turnosapp/novalidaingreso.html', context)
	
	context["DICMEDICOTMP"] = dicmedicotmp
	context["DICTURNOSTOMADOS"] = lista_diccionario_turnos

	return render(request, 'turnosapp/validaingreso.html', context)

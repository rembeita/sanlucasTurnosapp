from django.core.mail import send_mail
from turnosapp.models import Chc
from turnosapp.models import Turnos
from turnosapp.models import Dres
from turnosapp.models import Espec
from datetime import datetime, timedelta


def formatear_id_medico(idmedico):
	resultado = 4 - len(idmedico)
	return (" " * resultado) + idmedico

today = datetime.now()
tomorrow = today + timedelta(1)

print(today)
print(tomorrow.year)
print(tomorrow.month)
print(tomorrow.day)

turnos_list = Turnos.objects.all().filter( dia_tur__year=tomorrow.year, dia_tur__month=tomorrow.month, dia_tur__day= tomorrow.day)


for turno in turnos_list:
	print("###########")
	print(turno.id_chc)
	print(turno.nro_doc)
	print(turno.cod_esp)
	chc_info = Chc.objects.all().filter(id = turno.id_chc)
	paciente_nombre = chc_info.values()[0]['acciden']
	paciente_email = chc_info.values()[0]['sol_med2']
	print(paciente_email)
	print(paciente_nombre)
#	try:
	#if (paciente_email == ""):
	if (paciente_email.count("@") < 1):
		print("email vacio")
		continue
	print("Tiene email")
	doctor = Dres.objects.all().filter(cod_med = formatear_id_medico(turno.nro_doc))
	print(dir(doctor))
	print(doctor.values())
	doctor_nombre = doctor.values()[0]['nombre']
	print("no llegue")
	print(doctor_nombre)
	espec = Espec.objects.all().filter(cod_esp = formatear_id_medico(turno.cod_esp))
	espec_nombre = espec.values()[0]['nom_esp']
	print(espec_nombre)
	#send_mail('Recordatorio de turno', 'Estimado ' + paciente_nombre+ '.\n Le informamos que usted posee un turno el dia ' + tomorrow_day + ' a las ' + turno.hora_tur + ' con el medico ' + doctor_nombre + ' por la especialidad ' + espec_nombre + '.', 'turnos@sanlucas.com.ar', [paciente_email], fail_silently=False)
	print("ENVIANDOOOOOOO")
	send_mail('Recordatorio Turno San Lucas - ' +str(tomorrow.day) + '/'+ str(tomorrow.month)+' a las ' + turno.hora_tur, 'Estimado/a ' + paciente_nombre+ '.\nLe informamos que usted posee un turno el dia ' + str(tomorrow.day) + '/'+ str(tomorrow.month)+' a las ' + turno.hora_tur + ' con el profesional ' + doctor_nombre + '\nLa especialidad por la cual sera atendido/a es ' + espec_nombre + '.\nSi desea cancelar el turno puede hacerlo via web mediante la direccion http://www.sanlucas.com.ar/turnosapp las 24hs o por telefono a los siguientes numeros 011-5298-6350 en los horarios de 8 a 20hs.\n\n\nPor favor no responder a esta dirección de email. Ante cualquier consulta comuníquese con nosotros.', 'turnos@sanlucas.com.ar', [paciente_email], fail_silently=False)
#	except:
#		continue
		


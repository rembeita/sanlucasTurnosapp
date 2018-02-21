from django.core.mail import send_mail
from turnosapp.models import Chc
from turnosapp.models import Turnos
from turnosapp.models import Dres
from turnosapp.models import Espec
from datetime import datetime, timedelta
from django.core.mail import EmailMessage


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
	email = EmailMessage('Recordatorio Turno San Lucas - ' +str(tomorrow.day) + '/'+ str(tomorrow.month)+' a las ' + turno.hora_tur, 'Estimado/a ' + paciente_nombre+ '.\nLe informamos que usted posee un turno el dia ' + str(tomorrow.day) + '/'+ str(tomorrow.month)+' a las ' + turno.hora_tur + ' con el profesional ' + doctor_nombre + '\nLa especialidad por la cual sera atendido/a es ' + espec_nombre + '.\nSi desea cancelar el turno puede hacerlo via web mediante la direccion http://www.sanlucas.com.ar/turnosapp las 24hs o por telefono al numero 011-5298-6350 en los horarios de 8 a 20hs.\n\n\nPor favor no responder a esta dirección de email. Ante cualquier consulta comuníquese con nosotros.', 'turnos@sanlucas.com.ar', [ paciente_email ], [''], reply_to=['avisoturnos@cmmyo.com.ar'], headers={'Message-ID': 'foo'})
	img_data = open('/home/produccion/sanlucas/turnosapp/alertas_correo/firma.png', 'rb').read()
	email.attach('firma.png', img_data, 'image/png')
	email.send(fail_silently=False) 
	print("ENVIANDOOOOOOO")
	#send_mail('Recordatorio Turno San Lucas - ' +str(tomorrow.day) + '/'+ str(tomorrow.month)+' a las ' + turno.hora_tur, 'Estimado/a ' + paciente_nombre+ '.\nLe informamos que usted posee un turno el dia ' + str(tomorrow.day) + '/'+ str(tomorrow.month)+' a las ' + turno.hora_tur + ' con el profesional ' + doctor_nombre + '\nLa especialidad por la cual sera atendido/a es ' + espec_nombre + '.\nSi desea cancelar el turno puede hacerlo via web mediante la direccion http://www.sanlucas.com.ar/turnosapp las 24hs o por telefono al numero 011-5298-6350 en los horarios de 8 a 20hs.\n\n\nPor favor no responder a esta dirección de email. Ante cualquier consulta comuníquese con nosotros.', 'turnos@sanlucas.com.ar', [paciente_email], fail_silently=False)





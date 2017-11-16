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
from .models import Turcons
from .models import PacienteTurnoMedico

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

import time
from datetime import datetime
def finalturno(request):
    if request.method == 'POST':
        formvar = request.POST
        if (formvar.has_key('return')):
            if (str(formvar['return']) == 'Salir'):
                return HttpResponseRedirect('/turnosapp/')


    especialidadvalue = str(formvar['especialidad'])
    nombremedicovalue = str(formvar['nomMedico'])
    codmedvalue = str(formvar['codMedico'])
    codespvalue = str(formvar['codEspec'])
    nombrepacientevalue = str(formvar['nomPaciente'])          
    dnipacientevalue = str(formvar['dniPaciente'])
    fechavalue = str(formvar['fecha'])
    horariomedicovalue = str(formvar['horarioMedico'])
    fechadatabasevalue = str(formvar['fechaDatabase'])
    horadatabasevalue = str(formvar['horaDatabase'])
    horavalue = str(formvar['hora'])


    context = locals()    
    context["nomPaciente"] = nombrepacientevalue
    context["dniPaciente"] = dnipacientevalue
    context["especialidad"] = especialidadvalue 
    context["nomMedico"] = nombremedicovalue
    context["codMedico"] = codmedvalue
    context["codEspec"] = codespvalue
    context["fecha"] = fechavalue
    context["hora"] = horavalue
    context["horarioMedico"] = horariomedicovalue
    fechaDatabase = fechadatabasevalue
    horadatabasevalue = horadatabasevalue.replace(' ','')

    aplicarcambio = Tblhmed.objects.all().filter( medico = codmedvalue )
    aplicarcambio = aplicarcambio.filter( espec = codespvalue )
    aplicarcambio = aplicarcambio.filter( fecha = fechaDatabase )
    tblhmed_iden = aplicarcambio.values("id")[0]["id"]
    tblhmed_instance = Tblhmed.objects.get(id=tblhmed_iden)

    chc_info = Chc.objects.all().filter(nro_doc = dnipacientevalue)
    chc_id_value = str(chc_info.values("id")[0]["id"])
    chc_os_value = str(chc_info.values("cod_chc")[0]["cod_chc"])
    chc_nro_afil_value = str(chc_info.values("soc_chc")[0]["soc_chc"])
    chc_tele_value = str(chc_info.values("tele")[0]["tele"])
    chc_plan_value = str(chc_info.values("plan")[0]["plan"])
    chc_gravado_value = str(chc_info.values("gravado")[0]["gravado"])
    observ_value = " "
    wsvalue = "WWW"
    #consultorio = "0000"
    estadoturno = aplicarcambio.values(horadatabasevalue)[0][horadatabasevalue]
    codespvalue = codespvalue.strip()
#select * from turcons where fecha = '2016-09-06' and ESPEC  = '269' and doctor = '223';
    print( "#### NRO_DOC: " + codmedvalue)
    print( "#### NOMBRE_ESP: " + especialidadvalue)
    print( "#### COD_ESP: " + codespvalue)
    print( "#### ID_CHC: " + chc_id_value)
    print( "### DIA_TUR: " + fechavalue)
    print( "### O_SOCIAL: " + chc_os_value)
    print( "### NRO_AFIL: " + chc_nro_afil_value)
    print( "### TIPO_DOC: DNI")
    print( "### NO_DOC: " + dnipacientevalue)
    print( "### HORA_TUR: " + horavalue)
    print( "### DHM-TUR: " + str(fechaDatabase)) # FECHA COMPLETA DATE TIME
   # print( "### CONSULT: " + str(consultorio))
    print( "### TEL_TUR:" + chc_tele_value)
    print( "### PLAN:" + chc_plan_value)
    print( "### OBSERV:"  + observ_value)
    print( "### GRAVADO:"  + chc_gravado_value)
    print( "### USUARIO:"  + dnipacientevalue)
    print( "### WS: "  + wsvalue)
    print( "### FECALTA:"  + str(fechavalue)) # FUNCION DIA DE HOY
    print( "### HORAALTA:"  + str(horavalue))
    print("##### SQLESPECID: ")


    fecha_hora =  datetime.strptime(fechavalue + " " + horavalue, '%d-%m-%Y %H:%M')
    fecha_turno = datetime.strptime(fechavalue, '%d-%m-%Y')
    consultorio = Turcons.objects.all().filter(fecha = fecha_turno).filter(espec = codespvalue).filter(doctor = codmedvalue).values("consult")[0]["consult"]
    print( "### CONSULT: " + str(consultorio))
    
    hora_turno = datetime.strptime(horavalue, ' %H:%M')
    hora_turno = hora_turno.strftime("%H:%M")
    print("### HORA TURNO")
    print(hora_turno)

    # Verifico si la hora del turno comienza con 0 y la elimino. Solicitud Horacio
    if (hora_turno[0] == "0"):
        hora_turno = hora_turno[1:]

    dia_actual = time.strftime("%Y-%m-%d")
    hora_actual = time.strftime("%H:%M:%S")
    print(dia_actual)
    if (formvar.has_key('confirmar')):
	print("entre")
	print("estadoturno: " + estadoturno)
        if estadoturno == "X":
	    print("entre2")
            mensaje = "Su turno ha sido confirmado. Muchas Gracias."
            color    = "green"
            agregar_turno = Turnos(nro_doc=codmedvalue, cod_esp=codespvalue, id_chc=chc_id_value, dia_tur=fecha_turno, \
                    o_social=chc_os_value, nro_afil=chc_nro_afil_value, \
                    tipo_doc='DNI', no_doc=dnipacientevalue,hora_tur=hora_turno, \
                    #dhm_tur=fechaDatabase, consult=str(consultorio), \
                    dhm_tur=fecha_hora, consult=str(consultorio), \
                    tel_tur=chc_tele_value, plan=chc_plan_value, observ=observ_value, gravado=chc_gravado_value, \
                    usuario=dnipacientevalue, ws='WWW', \
#                    fecalta=str(fechavalue), horalta=str(horavalue))
                    fecalta=dia_actual, horalta=hora_actual, \
                    frec='0', importe='0.00', coseg='0.00', \
                    dia_modi=dia_actual, hs_modi=hora_actual)
            agregar_turno.save()
            ultimo_id = Turnos.objects.latest('id')
            chc_instance = Chc.objects.get(id=chc_id_value)
            aplicarcambio = aplicarcambio.update( **{horadatabasevalue: "C" })
	    
            agregar_relacion = PacienteTurnoMedico(turnos = ultimo_id, tblhmed = tblhmed_instance, chc = chc_instance, is_active = True)
            agregar_relacion.save()

        else:
            mensaje = "No se pudo confirmar el turno o el mismo se encuentra ocupado. Favor de volver a intentar."
            color   = "red"

        context["mensaje"] = mensaje
        context["color"] = color
        return render(request, 'turnosapp/finalturno.html', context)
    
    if (formvar.has_key('confirmareimprimir')):
        if estadoturno == "X":
            mensaje = "Su turno ha sido confirmado. Debera esperar 24hs antes de poder realizar cambios. Muchas Gracias."
            color    = "green"
            agregar_turno = Turnos(nro_doc=codmedvalue, cod_esp=codespvalue, id_chc=chc_id_value, dia_tur=fecha_turno, \
                    o_social=chc_os_value, nro_afil=chc_nro_afil_value, \
                    tipo_doc='DNI', no_doc=dnipacientevalue,hora_tur=hora_turno, \
                    #dhm_tur=fechaDatabase, consult=str(consultorio), \
                    dhm_tur=fecha_hora, consult=str(consultorio), \
                    tel_tur=chc_tele_value, plan=chc_plan_value, observ=observ_value, gravado=chc_gravado_value, \
                    usuario=dnipacientevalue, ws='WWW', \
#                    fecalta=str(fechavalue), horalta=str(horavalue))
                    fecalta=dia_actual, horalta=hora_actual, \
                    frec='0', importe='0.00', coseg='0.00', \
                    dia_modi=dia_actual, hs_modi=hora_actual)
            agregar_turno.save()
            ultimo_id = Turnos.objects.latest('id')
            chc_instance = Chc.objects.get(id=chc_id_value)
            aplicarcambio = aplicarcambio.update( **{horadatabasevalue: "C" })
	    
            agregar_relacion = PacienteTurnoMedico(turnos = ultimo_id, tblhmed = tblhmed_instance, chc = chc_instance, is_active = True)
            agregar_relacion.save()
            return render(request, 'turnosapp/finalturnopdf.html', context)
        else:
            mensaje = "No se pudo confirmar el turno o el mismo se encuentra ocupado. Favor de volver a intentar." 
            color   = "red"
            context["mensaje"] = mensaje
            context["color"] = color
            return render(request, 'turnosapp/finalturno.html', context)



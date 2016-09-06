# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosapp', '0005_paciente_turno_medico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente_turno_medico',
            name='chc_id',
        ),
        migrations.RemoveField(
            model_name='paciente_turno_medico',
            name='tblhmed_id',
        ),
        migrations.RemoveField(
            model_name='paciente_turno_medico',
            name='turnos_id',
        ),
        migrations.RemoveField(
            model_name='pacienteturnomedico',
            name='chc_id',
        ),
        migrations.RemoveField(
            model_name='pacienteturnomedico',
            name='tblhmed_id',
        ),
        migrations.RemoveField(
            model_name='pacienteturnomedico',
            name='turnos_id',
        ),
        migrations.DeleteModel(
            name='Paciente_Turno_Medico',
        ),
        migrations.DeleteModel(
            name='PacienteTurnoMedico',
        ),
    ]

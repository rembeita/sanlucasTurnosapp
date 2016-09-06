# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteTurnoMedico',
            fields=[
                ('auto_increment_id', models.AutoField(serialize=False, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('chc_id', models.ForeignKey(to='turnosapp.Chc')),
                ('tblhmed_id', models.ForeignKey(to='turnosapp.Tblhmed')),
                ('turnos_id', models.ForeignKey(to='turnosapp.Turnos')),
            ],
        ),
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
        migrations.DeleteModel(
            name='Paciente_Turno_Medico',
        ),
    ]

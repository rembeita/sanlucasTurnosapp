# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosapp', '0004_pacienteturnomedico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente_Turno_Medico',
            fields=[
                ('auto_increment_id', models.AutoField(serialize=False, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('chc_id', models.ForeignKey(to='turnosapp.Chc')),
                ('tblhmed_id', models.ForeignKey(to='turnosapp.Tblhmed')),
                ('turnos_id', models.ForeignKey(to='turnosapp.Turnos')),
            ],
        ),
    ]

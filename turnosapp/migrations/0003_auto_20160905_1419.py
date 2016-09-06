# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosapp', '0002_auto_20160905_1331'),
    ]

    operations = [
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
            name='PacienteTurnoMedico',
        ),
    ]

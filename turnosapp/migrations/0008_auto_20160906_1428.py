# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosapp', '0007_pacienteturnomedico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pacienteturnomedico',
            old_name='chc_id',
            new_name='chc',
        ),
        migrations.RenameField(
            model_name='pacienteturnomedico',
            old_name='tblhmed_id',
            new_name='tblhmed',
        ),
        migrations.RenameField(
            model_name='pacienteturnomedico',
            old_name='turnos_id',
            new_name='turnos',
        ),
    ]

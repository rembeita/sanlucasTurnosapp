# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosapp', '0006_auto_20160905_1426'),
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
    ]

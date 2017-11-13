#!/bin/bash
cd /home/produccion/sanlucas-development/
python manage.py shell < turnosapp/alertas_correo/enviarcorreo.py

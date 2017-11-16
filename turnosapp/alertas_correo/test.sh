#!/bin/bash
cd /home/produccion/sanlucas/
python manage.py shell < turnosapp/alertas_correo/enviarcorreo.py 

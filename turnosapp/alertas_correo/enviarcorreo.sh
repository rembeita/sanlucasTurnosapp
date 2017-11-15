#!/bin/bash
FECHA=$(date '+%Y-%m-%d %H:%M:%S')
cd /home/produccion/sanlucas/
echo "#############" >> /var/log/syslog
echo $FECHA >> /var/log/syslog
python manage.py shell < turnosapp/alertas_correo/enviarcorreo.py >> /var/log/syslog 2>&1
echo "#############" >> /var/log/syslog

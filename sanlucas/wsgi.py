"""
WSGI config for sanlucas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


sys.path.append('/home/produccion/sanlucas')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sanlucas.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "sanlucas.settings"

application = get_wsgi_application()

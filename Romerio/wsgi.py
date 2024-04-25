"""
WSGI config for MyDoors project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Romerio.settings')

application = get_wsgi_application()


# -*- coding: utf-8 -*-
import os, sys

sys.path.insert(0, '/var/www/u0000006/data/www/romerio.ru/Romerio')
sys.path.insert(1, '/var/www/u0000006/data/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Romerio.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

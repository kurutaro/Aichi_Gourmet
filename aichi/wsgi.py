"""
WSGI config for aichi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import pymysql
from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise


pymysql.install_as_MySQLdb()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aichi.settings')

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
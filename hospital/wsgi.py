"""
WSGI config for hospital project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

path = 'foldername'
if path not in sys.path:
  sys.path.append(path)

os.chdir(path)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')


from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

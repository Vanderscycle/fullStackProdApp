"""
WSGI config for prodHealthApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prodHealthApp.settings')

application = get_wsgi_application()

# with all the uswgi nightmares
#https://stackoverflow.com/questions/17555699/internal-server-error-with-django-and-uwsgi
# uwsgi --http :8000 --chdir ./src/ --wsgi-file '/home/henri/Documents/Post Lighthouse-Lab work/localFilesWebsite/src/prodHealthApp/wsgi.py'
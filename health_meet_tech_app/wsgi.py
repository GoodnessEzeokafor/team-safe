"""
WSGI config for health_meet_tech_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

# For Heroku

from django.core.wsgi import get_wsgi_application
from dj_static import Cling # heroku

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "health_meet_tech_app.settings")

application = get_wsgi_application()
application = Cling(get_wsgi_application()) #heroku


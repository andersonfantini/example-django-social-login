import os
import sys

HOME_PATH = "/var/www/django-login-social/"

# Add the app's directory to the PYTHONPATH
sys.path.append(HOME_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

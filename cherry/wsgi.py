# python imports
import os

# django imports
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cherry.settings")

application = get_wsgi_application()

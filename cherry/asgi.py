# python imports
import os

# django imports
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cherry.settings")

application = get_asgi_application()

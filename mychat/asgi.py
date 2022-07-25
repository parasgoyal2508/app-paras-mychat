"""
ASGI config for mychat project.

Interface between python servers, application.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychat.settings')

application = get_asgi_application()

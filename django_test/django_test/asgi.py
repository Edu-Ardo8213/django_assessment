"""
ASGI config for django_test project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django_test.routing import websocket_urlpatterns  # Asegúrate de tener tus rutas WebSocket aquí

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        websocket_urlpatterns
    ),
})

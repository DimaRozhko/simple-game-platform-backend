"""
ASGI config for sgp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from fifteen.routing import ws_fifteen_urlpatterns
from game.routing import ws_tic_tac_toe_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sgp.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(URLRouter([*ws_tic_tac_toe_urlpatterns, *ws_fifteen_urlpatterns]))
    }
)

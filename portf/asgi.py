"""
ASGI config for portf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack  # noqa: E402
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa: E402
from channels.sessions import SessionMiddlewareStack  # noqa: E402
from django.core.asgi import get_asgi_application
from reactpy_django import REACTPY_WEBSOCKET_PATH  # noqa: E402

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portf.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": SessionMiddlewareStack(
            AuthMiddlewareStack(URLRouter([REACTPY_WEBSOCKET_PATH]))
        ),
    }
)
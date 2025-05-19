from django.urls import re_path

from . import consumers

websocket_urlpatterns = [

        re_path(r"^room/(?P<room_name>[\w\s-]+)/$",consumers.CustomConsumer.as_asgi())
]

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/example/', consumers.ExampleConsumer.as_asgi()),
]

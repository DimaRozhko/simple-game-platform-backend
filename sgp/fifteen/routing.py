from django.urls import path
from fifteen.consumers import OneConsumer

ws_fifteen_urlpatterns = [
    path('ws/fifteen_url/', OneConsumer.as_asgi()),
]

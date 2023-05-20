from django.urls import path
from admininfo.consumers import OneConsumer

ws_admininfo_urlpatterns = [
    path('ws/admin_url/', OneConsumer.as_asgi()),
]

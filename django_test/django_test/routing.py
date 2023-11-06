from django.urls import re_path
from django_test.consumers import CreateCustomerConsumer

websocket_urlpatterns = [
    re_path(r'ws/create_customer/$', CreateCustomerConsumer.as_asgi())
]
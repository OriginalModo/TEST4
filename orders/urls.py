from django.urls import re_path
from .views import order_create, order_list

urlpatterns = [
    re_path(r'^orders/new/$', order_create, name='order_create'),
    re_path(r'^orders/$', order_list, name='order_list'),
]
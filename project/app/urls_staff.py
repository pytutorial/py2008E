from django.urls import path

from .views_staff import *

urlpatterns = [
    path('', listProduct),
]
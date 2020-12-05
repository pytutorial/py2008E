from django.urls import path
from .views import *

urlpatterns = [
    path('update-product/<pk>', ProductUpdateView.as_view()),
    path('create-product', ProductCreateView.as_view()),
    path('list-product', ProductListView.as_view()),
    path('hello2', HelloTemplateView.as_view()),
    path('hello', HelloView.as_view()),
    path('', index),
]
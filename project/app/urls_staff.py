from django.urls import path

from .views_staff import *

urlpatterns = [
    path('list-category', listCategory),
    path('create-category', CategoryCreateView.as_view()),

    path('', listProduct),
    path('create-product', ProductCreateView.as_view()),
]
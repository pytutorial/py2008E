from django.shortcuts import render
# Create your views here.
from .models import *

def index(request):#/
    name = request.GET.get('name', '')
    productList = Product.objects.filter(name__icontains=name)
    
    categoryId = request.GET.get('categoryId')
    if categoryId:
        categoryId = int(categoryId)
        productList = productList.filter(category__id=categoryId)
        
    priceRange = request.GET.get('priceRange')
    if priceRange:
        priceRange = int(priceRange)
        if priceRange == 1: #Duoi 10 trieu
            productList = productList.filter(price__lte=10e6)
        elif priceRange == 2: # Tren 10 trieu
            productList = productList.filter(price__gte=10e6)   

    categoryList = Category.objects.all()
    context = {
                'productList': productList, 
                'categoryList': categoryList,
                'name': name, 
                'categoryId': categoryId,
                'priceRange': priceRange,
            }
    return render(request, 'index.html', context)

def productDetail(request):
    id = request.GET.get('id')
    product = Product.objects.get(pk=id)
    return render(request, 'product.html', {'product': product})
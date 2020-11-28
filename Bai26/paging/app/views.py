from django.shortcuts import render
from .models import Product
import math
# Create your views here.
def index(request):
    PAGE_SIZE = 10
    name = request.GET.get('name', '')
    productList = Product.objects.filter(name__icontains=name)

    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    start = (page-1)*PAGE_SIZE
    end = start + PAGE_SIZE

    context  = {
        'productList': productList[start:end], 
        'name': name,
        'page': page,
        'num_page': math.ceil(len(productList)/PAGE_SIZE),
    }

    return render(request, 'index.html', context)
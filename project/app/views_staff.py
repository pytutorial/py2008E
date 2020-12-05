from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, UpdateView

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff/list-category'

def listCategory(request): #127.0.0.1:8000/staff/list-category
    categoryList = Category.objects.all()
    context = {'categoryList': categoryList}
    return render(request, 'staff/category/list.html', context)

def listProduct(request):
    return render(request, 'staff/product/list.html')
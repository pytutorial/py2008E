from django.shortcuts import render

def listProduct(request):
    return render(request, 'staff/product/list.html')
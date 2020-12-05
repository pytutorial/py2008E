from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product

class ProductCreateView(CreateView):#127.0.0.1:8000/create-product
    model = Product
    template_name = 'product_form.html'
    fields = '__all__'
    success_url = '/list-product'

class ProductUpdateView(UpdateView):#127.0.0.1:8000/update-product/1
    model = Product
    template_name = 'product_form.html'
    fields = '__all__'
    success_url = '/list-product'

class ProductListView(ListView):#127.0.0.1:8000/list-product
    template_name = 'product_list.html'
    context_object_name = 'productList'
    #queryset = Product.objects.all()
    def get_queryset(self):
        name = self.request.GET.get('name', '')
        return Product.objects.filter(name__icontains=name)

# Create your views here.
class HelloView(View):#127.0.0.1:8000/hello?name=Nguyen+Van+A
    def get(self, request, *arg, **kwargs):
        name = request.GET.get('name', '')
        context = {'name': name}
        return render(request, 'hello.html', context)

class HelloTemplateView(TemplateView):
    template_name = 'hello.html'
    def get_context_data(self, *arg, **kwargs):
        name = self.request.GET.get('name', '')
        return {'name': name}

def index(request):
    return render(request, 'index.html')


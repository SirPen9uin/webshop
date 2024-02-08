from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.


def index(request):
    template = 'index.html'
    products = Product.objects.all()
    context = {
        'products': products
    }
    if request.method == 'POST':
        pass
    return render(request, template)

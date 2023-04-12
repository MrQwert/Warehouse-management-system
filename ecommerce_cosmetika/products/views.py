from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    context = {'products': products, 'form': CartAddProductForm()}
    return render(request, 'products/index.html', context)

from django.shortcuts import render
from products.models import Product

# Create your views here.
def ProductList(request):
    products = Product.objects.all()  # Or any queryset you need
    return render(request, 'productlist.html', {'products': products})
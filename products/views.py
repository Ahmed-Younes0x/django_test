from django.shortcuts import render,redirect
from products.models import Product

# Create your views here.
def ProductList(request):
    products = Product.objects.all()  # Or any queryset you need
    return render(request, 'productlist.html', {'products': products})

def AddProduct(request):
    if request.method=='POST':
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            creation_date=request.POST.get('creation_date'),
            ex_date=request.POST.get('ex_date'),
            country=request.POST.get('country'),
            price=request.POST.get('price'),
            cat=request.POST.get('cat'),
            image=request.FILES['image']
        )
        return redirect('addproduct')
    else:
        return render(request, 'productform.html')
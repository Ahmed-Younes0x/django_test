from django.shortcuts import render,redirect
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginform')
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
    
def Update_Product(request,id):
    product=Product.objects.get(id=id)
    if request.method=='POST':
            product.description=request.POST['description']
            product.creation_date=request.POST['creation_date']
            product.ex_date=request.POST['ex_date']
            product.price=request.POST['price']
            print(request.POST['description'],
            request.POST['creation_date'],
            request.POST['ex_date'],
            request.POST['price'])
            product.save()
            return redirect(ProductList)
    else:
        return render(request, 'updateform.html', context={'product': product})
def Delete_Product(request,id):
        prod=Product.objects.get(id=id)
        if prod:
            prod.delete()
            return redirect(ProductList)
        else:
            return render(request, 'deleteform.html')
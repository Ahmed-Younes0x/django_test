from django.shortcuts import render,redirect
from products.models import Product, category
from django.contrib.auth.decorators import login_required
from django.views import View
from . import forms


class ProductList(View):
    def get(self,request):
        products = Product.objects.all() 
        return render(request, 'productlist.html', {'products': products})

class AddProduct(View):
    def post(self,request):
        # Product.objects.create(
        #     name=request.POST.get('name'),
        #     description=request.POST.get('description'),
        #     creation_date=request.POST.get('creation_date'),
        #     ex_date=request.POST.get('ex_date'),
        #     country=request.POST.get('country'),
        #     price=request.POST.get('price'),
        #     cat=request.POST.get('cat'),
        #     image=request.FILES['image']
        # )
        form= forms.Addproduct(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('addproduct')
    def get(self,request):
        form= forms.Addproduct()
        return render(request, 'productform.html', context={'form': form})
        

    
class Update_Product(View):
    def post(self,request,id):
        form=forms.Update_product_Form(request.POST,request.FILES)
        if form.is_valid():
            product=Product.objects.get(id=id)
            product.description=request.POST['description']
            product.creation_date=request.POST['creation_date']
            product.ex_date=request.POST['ex_date']
            product.price=request.POST['price']
            product.image=request.FILES['image']
            product.save()
            return redirect('p_list')
        else:
            return redirect('home')
    def get(self,request,id):
        product=Product.objects.get(id=id)
        form=forms.Update_product_Form()
        return render(request, 'updateform.html', context={'product': product, 'form': form})


class Delete_Product(View):
    def get(self,request,id):
        prod=Product.objects.get(id=id)
        if prod:
            prod.delete()
            return redirect(ProductList)
        else:
            return render(request, 'deleteform.html')
        
class AddCategory(View):
    def get(self,request):
        form=forms.AddCat()
        return render(request,'addcat.html',context={'category': category.objects.all(),'form': form})
    
    def post(self,request):
        form=forms.AddCat(request.POST)
        if form.is_valid() and not category.objects.filter(name=request.POST['name']):
            newCat=category.objects.create(name=request.POST['name'])
            newCat.save()
            success=True
        else:
            success=False
        return render(request,'addcat.html',context={'category': category.objects.all(),'success': success,'form': forms.AddCat()})

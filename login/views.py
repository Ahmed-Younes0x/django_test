from django.shortcuts import redirect, render
from django.contrib.auth import logout,login,authenticate
# from login.models import User
from django.contrib.auth.models import User

from products.views import ProductList
from django.contrib.sessions.models import Session

# Create your views here.
def register_user(request):
    if request.method=='POST':
        User.objects.create_user(
        username = request.POST['name'],
        password = request.POST['password'],
        email = request.POST['email']
        )
        return render(request,'registerform.html')
    else:
        return render(request,'registerform.html')

def loginn(request):
    if request.method=='POST':
        username = request.POST['name'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            print('user logged in')
            login(request,user)
            request.session['username'] = user.username
            request.session.save()
            return redirect(ProductList)
        else:
            return redirect(register_user)
    else:
        return render(request,'loginform.html')
    
def logout_view(request):
    logout(request)
    Session.objects.filter(session_key=request.session.session_key).delete()
    return redirect('home')
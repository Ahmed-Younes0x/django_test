from django.shortcuts import redirect, render
from django.contrib.auth import logout,login,authenticate
# from login.models import User
from django.contrib.auth.models import User
from django.views import View
from django.contrib.sessions.models import Session
from .forms import register_form

# Create your views here.
class register_user(View):

    def post(self,request):
        form=register_form(request.POST)
        User.objects.create_user(
        username = request.POST['name'],
        password = request.POST['password'],
        email = request.POST['email']
        )
        return render(request,'registerform.html')
    def get(self,request):
        form=register_form()
        return render(request,'registerform.html',context={'form':form})

class loginn(View):
    def post(self,request):
        username = request.POST['name'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            print('user logged in')
            login(request,user)
            request.session['username'] = user.username
            request.session.save()
            return redirect('p_list')
        else:
            return redirect('regform')
    
    def get(self,request):
        return render(request,'loginform.html')
    
def logoutt(request):
    logout(request)
    Session.objects.filter(session_key=request.session.session_key).delete()
    return redirect('home')
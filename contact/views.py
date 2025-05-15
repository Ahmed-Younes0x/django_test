from django.shortcuts import render,HttpResponse
from django.template import loader

# Create your views here.
def contact(request):
    return render(request,'contact.html')
"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from contact.views import contact
from home.views import home
from login.views import loginn, logoutt, register_user
from settings.views import settings
from products.views import Delete_Product, ProductList,AddProduct, Update_Product, AddCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ProductList.as_view(),name='default'),
    path('contact',contact,name='contact'),
    path('settings',settings,name='settings'),
    path('home',home,name='home'),
    path('products',ProductList.as_view(),name='p_list'),
    path('addproduct',AddProduct.as_view(),name='addproduct'),
    path('addcat',AddCategory.as_view(),name='addcat'),
    path('updateproduct/<int:id>',Update_Product.as_view(),name='updateproduct'),
    path('deleteproduct/<int:id>',Delete_Product.as_view(),name='deleteproduct'),
    path('register',register_user.as_view(),name='regform'),
    path('login',loginn.as_view(),name='loginform'),
    path('logout',logoutt,name='logout'),
    path('myapi', include('myapi.urls')),
]

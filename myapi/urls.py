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
from rest_framework import routers
from .views import CategoryApi, ProductApiViewSet, UserApi
# router = routers.DefaultRouter()
# router.register(r'category', CategoryApi, basename='CategoryApi')

urlpatterns = [
    path('/UserApi',UserApi),
    path('/ProductApi',ProductApiViewSet.as_view()),
    path('/CategoryApi',CategoryApi.as_view({'get':'list','post':'create','put':'partial_update','delete':'delete'})),
]
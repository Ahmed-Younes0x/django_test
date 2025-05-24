from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK,HTTP_404_NOT_FOUND
from django.contrib.auth.models import User
from rest_framework.views import APIView

from products.models import Product, category

from .serializers import CategorySerializer, ProductSerializer, UserSerializer

# Create your views here.
@api_view(('GET','POST'))
def UserApi(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(serializer._validated_data)
            return Response({'data':serializer.data},status=HTTP_200_OK)
        return Response({'data':[]},status=HTTP_404_NOT_FOUND)
    else:
        print('here')
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response({'message':'g','data':serializer.data},status=HTTP_200_OK)


class ProductApiViewSet(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(data=products,many=True)
        if serializer.is_valid():
            return Response({'data':serializer.data},status=HTTP_200_OK)
        return Response({'data':serializer.data},status=HTTP_404_NOT_FOUND)
    
    def post(self,request):
        data=request.data
        data['cat_obj']=int(data['cat_obj'][1])
        files=request.FILES
        serializer=ProductSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            print('here product')
            serializer.save()
            return Response({'message':'added','data':"serializer.data"},status=HTTP_200_OK)
        return Response({'message':serializer.errors},status=HTTP_404_NOT_FOUND)
    
class CategoryApi(viewsets.ViewSet):
        def list(self, request):
            queryset = category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
            return Response(serializer.data)
        
        def create(self, request):
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                category.objects.create(**serializer._validated_data)
            return Response(serializer.data)
        
    
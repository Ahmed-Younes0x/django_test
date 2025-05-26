from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User
from rest_framework.views import APIView

from products.models import Product, category

from .serializers import CategorySerializer, ProductSerializer, UserSerializer

# Create your views here.
@api_view(('GET','POST','DELETE','PUT'))
def UserApi(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response({'data':serializer.data},status=HTTP_200_OK)
        return Response({'data':[]},status=HTTP_404_NOT_FOUND)
    elif request.method=='GET':
        print('here')
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response({'message':'g','data':serializer.data},status=HTTP_200_OK)
    elif request.method == 'PUT':
        user = User.objects.get(email=request.data.get('email'))
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(validated_data=serializer.validated_data,instance=user)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user = User.objects.get(username=request.data.get('username'))
        user.delete()
        return Response(
            {'message': 'User deleted successfully'}, 
            status=HTTP_204_NO_CONTENT
        )


class ProductApiViewSet(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(data=products,many=True)
        if serializer.is_valid():
            return Response({'data':serializer.data},status=HTTP_200_OK)
        return Response({'data':serializer.data},status=HTTP_404_NOT_FOUND)
    
    def post(self,request):
        data=request.data
        # data['cat_obj']=int(data['cat_obj'][1])
        files=request.FILES
        print('here product')
        serializer=ProductSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            print('here product')
            serializer.save()
            return Response({'message':'added','data':serializer.data},status=HTTP_200_OK)
        return Response({'message':serializer.errors},status=HTTP_404_NOT_FOUND)
    
    def put(self,request):
        product=Product.objects.get(name=request.data.get('name'))
        serializer=ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.update(product,serializer.validated_data)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        product=Product.objects.get(name=request.data.get('name'))   
        product.delete() 
        return Response(
            {'message': 'product deleted successfully'}, 
            status=HTTP_204_NO_CONTENT
        )
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
        def delete(self,request):
            queryset = category.objects.get(name=request.data.get('name'))
            queryset.delete()
            return Response(
                {'message': 'category deleted successfully'}, 
                status=HTTP_204_NO_CONTENT
            )
        def partial_update(self,request):
            product=category.objects.get(name=request.data.get('query'))
            serializer=CategorySerializer(product,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.update(product,serializer.validated_data)
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)        
    
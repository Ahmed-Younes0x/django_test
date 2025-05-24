from rest_framework import serializers
from products.models import Product

class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50)
    email = serializers.EmailField()
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'
        extra_kwargs = {'image': {'required': True}}
    
class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)



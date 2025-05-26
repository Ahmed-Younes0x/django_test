from rest_framework import serializers
from products.models import Product

class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50)
    email = serializers.EmailField()
    def update(self,instance,validated_data):
        for attrip, value in validated_data.items():
            setattr(instance, attrip, value)
        instance.save()
        return instance
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        # fields = '__all__'
        exclude = ['cat_obj']
        extra_kwargs = {'image': {'required': True}}
    
class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    def update(self,instance,validated_data):
        for attrip, value in validated_data.items():
            setattr(instance, attrip, value)
        instance.save()
        return instance


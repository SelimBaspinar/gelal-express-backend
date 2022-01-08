from rest_framework import serializers
from .models import Category,SubCategory,Product



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields =  "__all__"   


class SubCategorySerializer(serializers.ModelSerializer):
    categories=serializers.CharField(read_only=True)
   

    class Meta:
        model = SubCategory
        fields =  "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"  


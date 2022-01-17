from rest_framework import fields,serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= (
            'id',
            'name',
            'description',
            'price',
            'image',
            'date_added'
        )
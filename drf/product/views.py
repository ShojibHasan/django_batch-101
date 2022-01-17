from django.http.response import Http404
from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product,Category
# Create your views here.


class LatestProductList(APIView):
    def get(self,request,format = None):
        products = Product.objects.all()[0:3]
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get_object(self,category_id,product_id):
        try:
            return Product.objects.filter(category__id=category_id).get(id=product_id)
        except Product.DoesNotExist:
            return Http404
    
    def get(self,request, category_id,product_id,format=None):
        product = self.get_object(category_id,product_id)
        # print(product)
        serializer=ProductSerializer(product)
        # print(serializer.data)
        return Response(serializer.data)
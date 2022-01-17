from django.urls import path,include
from product import views

urlpatterns = [
    path('latest_products/',views.LatestProductList.as_view(),name="latest_products"),
    path('products/<int:category_id>/<int:product_id>/',views.ProductDetail.as_view(),name='product_details')
]

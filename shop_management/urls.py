from django.urls import path

from . import product_details

urlpatterns = [
    # path('product_list', product_details.get_list_of_products, name='product_list'),
    path('product_details', product_details.ProductDetails.as_view(), name='add_product_details'),
]
from django.db import models

# Create your models here.

class ProductDetail(models.Model):
    """
    This table contains product  details
    """
    product_id = models.BigAutoField(db_index=True, primary_key=True)
    name = models.TextField( max_length=255, unique=True,null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    details = models.CharField( max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
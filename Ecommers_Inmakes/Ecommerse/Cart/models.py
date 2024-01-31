from django.db import models
from shop.models import *
# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_time_field=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering=['date_time_field']
    
    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quntity=models.IntegerField()
    active=models.BooleanField(default=True)
    
    class Meta:
        db_table = 'CartItem'
    
    def sub_total(self):
        return self.product.price*self.quntity
    
    def __str__(self):
        return self.product.name

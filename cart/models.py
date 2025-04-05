from django.db import models
from store.models import product

class Cart(models.Model):
    cart_id=models.CharField(max_length=234,blank=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.product
    

from django.db import models
from app1.models import category
from django.urls import reverse

class product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    discription=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='images')
    stock=models.IntegerField()
    is_avalible=models.BooleanField(default=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE,related_name="products")
    related_products = models.ManyToManyField('self', blank=True, symmetrical=False, related_name="related_to")
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)



    def get_url(self):
        return reverse('product_details',args=[self.category.slug, self.slug])




    def __str__(self):
        return self.product_name
    
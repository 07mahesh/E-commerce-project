from django.db import models
from django.urls import reverse

class category(models.Model):
    category_name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(max_length=234, blank=True)
    cat_img = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])


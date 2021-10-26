from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_name     = models.CharField(max_length=200, unique=True)
    slug             = models.SlugField(max_length=200, unique=True)
    description      = models.TextField(max_length=500, blank=True)
    price            = models.IntegerField(default=0)
    old_price        = models.IntegerField(default=0)
    images           = models.ImageField(upload_to='photos/products', blank=True)
    stock            = models.IntegerField(default=100)
    is_available     = models.BooleanField(default=True)
    created_date     = models.DateTimeField(auto_now_add=True)
    modified_date    = models.DateTimeField(auto_now=True)
    category         = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('product_datail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

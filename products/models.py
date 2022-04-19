from django.db import models
from account.models import UserBase
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager,self).get_queryset().filter(is_active=True)

class Category(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    slug_title = models.SlugField(max_length=300,unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:category_list',args=[self.slug_title,])

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserBase,on_delete=models.CASCADE,related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/',default='images/product/default.png')
    slug= models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('products:product-detail',args=[self.slug,])


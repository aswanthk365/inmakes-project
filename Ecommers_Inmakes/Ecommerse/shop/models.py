from django.db import models
from django.urls import reverse
# Create your models here.


class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    discriptioin=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)
 
    def get_url(self): 
        return reverse('shop:product_categ',args=[self.slug])

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    discriptioin=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    categorys=models.ForeignKey(category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products')
    stock=models.IntegerField()
    avilabilty=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_url(self): 
        return reverse('shop:product_deatails',args=[self.categorys.slug,self.slug])

class comment(models.Model):
    user_name=models.CharField(max_length=250)#Set user name
    comments=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(product,on_delete=models.CASCADE)

    def __str__(self):
        return '%s , %s' % (self.product.name,self.user_name)
from django.db import models
from catagory.models import Catagory
from django.urls import reverse
# Create your models here.
class Technology(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.TextField(max_length=500,blank=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='photos/product/')
    stock=models.IntegerField()
    doc_url=models.CharField(max_length=200,unique=True)
    doc_video=models.CharField(max_length=200,unique=True)
    is_available=models.BooleanField(default=True)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name='technology'
        verbose_name_plural='technologies'

    def __str__(self):
        return self.product_name
class AboutMe(models.Model):
    header=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255,blank=True)
    title=models.CharField(max_length=400,unique=True)
    my_image=models.ImageField(upload_to='photoes/aboutme/',blank=True)

    def __str__(self):
        return self.header

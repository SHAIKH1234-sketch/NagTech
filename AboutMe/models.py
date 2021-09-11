from django.db import models

# Create your models here.
class AboutMe(models.Model):
    header=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255,blank=True)
    title=models.CharField(max_length=400,unique=True)
    my_image=models.ImageField(upload_to='photoes/aboutme/',blank=True)

    def __str__(self):
        return self.header

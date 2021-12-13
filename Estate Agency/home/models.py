from django.db import models
from accounts.models import User
from embed_video.fields import EmbedVideoField
# Create your models here.



class Property(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="property/")
    location = models.CharField(max_length=250)
    property_type =models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    beds = models.CharField(max_length=250)
    baths =models.CharField(max_length=250)
    garage =models.CharField(max_length=250)
    video = EmbedVideoField(blank=True,null=True)
    date_added = models.DateField(auto_now_add=True)
    is_publish = models.BooleanField(default=False)
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    

    
class Slider(models.Model):
    image = models.ImageField(upload_to="slider/")
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.property.name
    
class Inquary(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name =models.CharField(max_length=250,blank=True,null=True)
    email =models.CharField(max_length=250,blank=True,null=True)
    phone =models.CharField(max_length=15,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
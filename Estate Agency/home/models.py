from django.db import models

# Create your models here.



class Property(models.Model):
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
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    

    
class Slider(models.Model):
    image = models.ImageField(upload_to="slider/")
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.property.name
    

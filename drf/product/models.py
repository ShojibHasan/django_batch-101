from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to = 'uploads/',blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering =('-date_added',)
        
    def __str__(self):
        return self.name
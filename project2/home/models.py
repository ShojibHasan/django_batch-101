from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    standerd = models.CharField(max_length=20)
    image = models.ImageField(upload_to='student_images/')
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    previous_school = models.CharField(max_length=200)
    previous_result = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student
    list_display = ['name','standerd','phone','address','previous_school','previous_result']

admin.site.register(Student,StudentAdmin)
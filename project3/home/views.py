from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST' and request.FILES['image']:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        image = request.FILES['image']
        
        if Student.objects.filter(username=user_name).exists():
            messages.success(request,'Username Already Taken ')
        else:
            Student.objects.create(first_name=first_name,last_name=last_name,department=department,username=user_name,email=email,contact_no=contact_no,image=image)
            messages.success(request,'Student Created ')
        
    return render(request, 'registration.html')
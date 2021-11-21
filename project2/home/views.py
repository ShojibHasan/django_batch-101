from django.shortcuts import render
from .models import Student
from django.contrib import messages
# Create your views here.

# a = 10

def student_registration(request):
    if request.method == 'POST' and request.FILES['image']:
        sname = request.POST.get('sname')
        standerd = request.POST.get('standerd')
        phone = request.POST.get('phone') 
        address = request.POST.get('address')
        previous_school = request.POST.get('previous_school') 
        previous_result = request.POST.get('previous_result') 
        image = request.FILES['image']
        
        
        
        if not Student.objects.filter(phone=phone).exists():
            Student.objects.create(name=sname,standerd=standerd,image=image,phone=phone,address=address,previous_school=previous_school,previous_result=previous_result)
            messages.success(request,'Student Registration Successfully')
            # return render(request, 'student/registration.html')
        
        else:
            messages.success(request,'ERROR!! Try Diffrent number')

    return render(request, 'student/registration.html')
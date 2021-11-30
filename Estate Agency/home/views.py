
from django.shortcuts import render

from home.models import Property, Slider
from django.core.paginator import Paginator

# Create your views here.



def home(request):
    slider = Slider.objects.all()
    porperty = Property.objects.all()
    context = {
        'slider':slider,
        'porperty':porperty,
    }
    return render(request, 'home/index.html',context)

def all_property(request):
    property_list = Property.objects.all()
    paginator = Paginator(property_list,3)
    page_number = request.GET.get('page')
    property = paginator.get_page(page_number)
    
    context = {
        'property':property,
    }
    return render(request,'home/all_property.html',context)

def single_property(request,id):
    property = Property.objects.get(id=id)
    context = {
        'property':property
    }
    return render(request,'home/single_property.html',context)
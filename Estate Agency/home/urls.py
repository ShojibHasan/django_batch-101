
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('all_property/',views.all_property,name="all_property"),
    path('property/<int:id>',views.single_property,name="single_property"),
]

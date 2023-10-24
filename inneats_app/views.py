from django.shortcuts import get_object_or_404, render, redirect
from .models import HotelCounts
# from django.db.models import Q 
# from django.http import HttpResponse, JsonResponse
# import json
# from django.core import serializers

def index(request):
    return render(request, 'inneats_app/index.html')
    
def about(request):    
    return render(request, 'inneats_app/about.html')

def property_list(request):
    return render(request, 'inneats_app/property-list.html')

def property_type(request):     
    return render(request, 'inneats_app/property-type.html')

def properties(request):
    hotel_data = HotelCounts.objects.all()
    context = {'hotel_data': hotel_data}
    return render(request, 'inneats_app/properties.html', context)

def property_testimonial(request):
    return render(request, 'inneats_app/testimonial.html')

def error404(request):
    return render(request, 'inneats_app/404.html')

def contact(request):
    return render(request, 'inneats_app/contact.html')







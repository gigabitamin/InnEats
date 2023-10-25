# from django.http import HttpResponse, JsonResponse
# from django.core import serializers
# import json
# from .models import NaverBlog
# from .models import Youtube
# from django.db.models import Q
# from .forms import YoutubeForm
# from .forms import NaverBlogForm
# from .forms import UserInfoForm
# from .forms import ImageForm

from django.shortcuts import get_object_or_404, render, redirect
from .models import Hotelcounts


def index(request):
    user_info = request.user
    hotel_data = Hotelcounts.objects.all()

    return render(request, 'inneats_app/index.html', {'user_info':user_info,'hotel_data':hotel_data})
    
def about(request):    
    return render(request, 'inneats_app/about.html')

def property_list(request):
    return render(request, 'inneats_app/property-list.html')

def property_type(request):     
    return render(request, 'inneats_app/property-type.html')

def property_agent(request):
    return render(request, 'inneats_app/property-agent.html')

def property_testimonial(request):
    return render(request, 'inneats_app/testimonial.html')

def error404(request):
    return render(request, 'inneats_app/404.html')

def contact(request):
    return render(request, 'inneats_app/contact.html')


def property_agent(request):
    hotel_data = Hotelcounts.objects.all()
    # context = {'hotel_data': hotel_data}
    return render(request, 'inneats_app/index.html', {'hotel_data':hotel_data})







from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('property/list/', views.property_list, name='property_list'),
    path('property/type/', views.property_type, name='property_type'),
    path('property/agent/', views.property_agent, name='property_agent'),
    path('property/testimonial/', views.property_testimonial, name='property_testimonial'),
    path('error404/', views.error404, name='error404'),
    path('contact/', views.contact, name='contact')
]

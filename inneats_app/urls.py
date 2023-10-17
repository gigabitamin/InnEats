
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='about'),
    path('', views.index, name='property_list'),
    path('', views.index, name='property_type'),
    path('', views.index, name='property_agent'),
    path('', views.index, name='property_testimonial'),
    path('', views.index, name='error404'),
    path('', views.index, name='contact'),    

]

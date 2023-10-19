
from django.urls import path
from . import views

urlpatterns = [
    path('accommodation/', views.accommodation, name='accommodation'),
    path('accommodation_detail/', views.accommodation_detail, name='accommodation_detail'),
]

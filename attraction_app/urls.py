
from django.urls import path
from . import views

urlpatterns = [
    path('attraction/<str:keyword>', views.attraction, name='attraction'),
    
]

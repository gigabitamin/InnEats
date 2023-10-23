
from django.urls import path
from . import views

urlpatterns = [
    path('attraction/', views.attraction, name='attraction'),
]

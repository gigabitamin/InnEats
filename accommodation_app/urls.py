
from django.urls import path
from . import views

urlpatterns = [
    path('accommodation/', views.accommodation, name='accommodation'),
]

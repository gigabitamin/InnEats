from django.urls import path
from . import views

urlpatterns = [
    path('sjh_app/', views.sjh_app, name='sjh_app'),
]

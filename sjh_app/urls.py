from django.urls import path
from . import views

urlpatterns = [
    path('sjh_app/', views.sjh_app, name='sjh_app'),
    path('display_map/', views.display_map, name='display_map'),
]

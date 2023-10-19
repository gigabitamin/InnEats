
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("inneats_app.urls")),    
    path('users/', include("users_app.urls")), 
    
    # accommodation_app 추가 - 김영재
    path('users/', include("accommodation_app.urls")),    
]

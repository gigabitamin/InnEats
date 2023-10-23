from django.shortcuts import render

# Create your views here.
def attraction(request):    
    
    return render(request, 'attraction_app/attraction.html')
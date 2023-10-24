from django.shortcuts import render

# Create your views here.
def sjh_app(request):
    return render(request, 'sjh_app/map_detail.html')

def display_map(request):
    return render(request, 'sjh_app/map_aewol.html')
from django.shortcuts import render

# Create your views here.
def map_main(request):
    return render(request, 'sjh_app/map_main.html')

def display_map(request):
    return render(request, 'sjh_app/map_aewol.html')

# Create your views here.
def map_detail(request):
    return render(request, 'sjh_app/map_detail.html')


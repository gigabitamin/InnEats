from django.shortcuts import render

# Create your views here.
def sjh_app(request):
    return render(request, 'sjh_app/map_detail.html')
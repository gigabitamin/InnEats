from django.shortcuts import render

# Create your views here.
def accommodation(request):    

    return render(request, 'accommodation_app/accommodation.html')


def accommodation_detail(request):    

    return render(request, 'accommodation_app/accommodation_detail.html')
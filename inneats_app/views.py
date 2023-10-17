from django.shortcuts import render

def index(request):
    return render(request, 'inneats_app/index.html')

def about(request):
    return render(request, 'inneats_app/about.html')

def property_list(request):
    return render(request, 'inneats_app/property-list.html')

def property_type(request):
    return render(request, 'inneats_app/property-type.html.html')

def property_agent(request):
    return render(request, 'inneats_app/property-agent.html.html')

def property_testimonial(request):
    return render(request, 'inneats_app/testimonial.html')

def error404(request):
    return render(request, 'inneats_app/404.html')

def contact(request):
    return render(request, 'inneats_app/contact.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def error(request):
    return render(request, '404.html')

def contact(request):
    return render(request, 'contact.html')

def new(request):
    return render(request, 'new.html')

def single(request):
    return render(request, 'single.html')

def specials(request):
    return render(request, 'specials.html')
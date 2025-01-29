from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def construction(request):
    return render(request, 'pages/construction.html')

def agriculture(request):
    return render(request, 'pages/agriculture.html')
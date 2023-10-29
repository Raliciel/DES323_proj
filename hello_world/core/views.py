from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "web/index.html", context)

def home(request):
    context = {
        "title": "Home Page"
    }
    return render(request, "web/home.html", context)
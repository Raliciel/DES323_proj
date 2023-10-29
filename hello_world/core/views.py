from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "web/index.html", context)


def setting(request):
    context = {
        "title": "Setting Example",
    }
    return render(request, "web/settings.html",context)


def home(request):
    context = {
        "title": "Home Example",
    }
    return render(request, "web/home.html",context)

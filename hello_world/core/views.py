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
    return render(request, "web/setting.html",context)
from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "web/index.html", context)

<<<<<<< HEAD

def setting(request):
    context = {
        "title": "Setting Example",
    }
    return render(request, "web/setting.html",context)
=======
def home(request):
    context = {
        "title": "Home Page"
    }
    return render(request, "web/home.html", context)
>>>>>>> fdea4a5084f682ab5e51e1cfcb3c8d9fe0df6409

from django.shortcuts import render
from .models import *
# Create your views here.
def database_item_list_all(request):
    dataset_objs = setting.objects.all()
    context_data = {
        "filter_type":"All",
        "datasets":dataset_objs
    }
    return render(request, 'database/list_view.html', context= context_data)

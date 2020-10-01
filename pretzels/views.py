from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pretzels

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Home View</h1>")

def pretzel_detail_view(request, pretzel_id, *args, **kwargs):
    try:
        obj = Pretzels.objects.get(id = pretzel_id)
    except:
        raise Http404
    return HttpResponse(f'<h1>Pretzel {pretzel_id} - {obj.content} </h1>')
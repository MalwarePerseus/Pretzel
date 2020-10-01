from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Pretzels

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Home View</h1>")

def pretzel_detail_view(request, pretzel_id, *args, **kwargs):

    data = {
        "id" : pretzel_id,
    }
    
    status = 200

    try:
        obj = Pretzels.objects.get(id = pretzel_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status = status)
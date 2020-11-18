from django.http import HttpResponse
from DoesItStinkBYUData import selectAllBathrooms
import json

def indexPageView(request):
    bathrooms = selectAllBathrooms()
    return HttpResponse("{\"buildings\": " + json.dumps([o.dump() for o in bathrooms]) + "}")

from django.http import HttpResponse
from DoesItStinkBYUData import selectAllBuildings
import json

def indexPageView(request):
    buildings = selectAllBuildings()
    return HttpResponse("{\"buildings\": " + json.dumps([building.dump() for building in buildings]) + "}")

from django.http import HttpResponse
from DoesItStinkBYUData import selectAllBuildings
import json

def indexPageView(request):
    buildings = selectAllBuildings()
    return HttpResponse(json.dumps([o.dump() for o in buildings]))

from django.http import HttpResponse
from DoesItStinkBYUData import selectLeaders
import json

def indexPageView(request, time):
    leaders = selectLeaders(time)
    return HttpResponse("{\"leaders\": " + json.dumps([o.dump() for o in leaders])+ "}")

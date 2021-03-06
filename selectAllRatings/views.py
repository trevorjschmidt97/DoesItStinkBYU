from django.http import HttpResponse
from DoesItStinkBYUData import selectAllRatings
import json

def indexPageView(request):
    ratings = selectAllRatings()
    return HttpResponse("{\"ratings\": " + json.dumps([o.dump() for o in ratings]) + "}")

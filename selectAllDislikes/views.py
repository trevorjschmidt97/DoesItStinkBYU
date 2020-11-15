from django.http import HttpResponse
from DoesItStinkBYUData import selectAllDislikes
import json

def indexPageView(request):
    dislikes = selectAllDislikes()
    return HttpResponse(json.dumps([o.dump() for o in dislikes]))

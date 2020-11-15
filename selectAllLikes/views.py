from django.http import HttpResponse
from DoesItStinkBYUData import selectAllLikes
import json

def indexPageView(request):
    likes = selectAllLikes()
    return HttpResponse(json.dumps([o.dump() for o in likes]))

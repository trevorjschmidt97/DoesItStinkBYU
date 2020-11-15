from django.http import HttpResponse
from DoesItStinkBYUData import selectAllReviews
import json

def indexPageView(request):
    reviews = selectAllReviews()
    return HttpResponse(json.dumps([o.dump() for o in reviews]))

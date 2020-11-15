from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import selectReviewsInBathroom
import json

def indexPageView(request, bathroomID, sort):
    reviews = selectReviewsInBathroom(bathroomID, sort)
    return HttpResponse(json.dumps([o.dump() for o in reviews]))

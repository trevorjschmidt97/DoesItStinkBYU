from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import selectReviewsInBathroom
import json

def indexPageView(request, bathroomID, sort, userID):
    reviews = selectReviewsInBathroom(bathroomID, sort, userID)
    return HttpResponse("{\"reviews\": " + json.dumps([o.dump() for o in reviews]) + "}")

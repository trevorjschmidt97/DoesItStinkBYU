from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import selectInfoAndReviewsInBathroom
import json

def indexPageView(request, bathroomID):
    infoAndReviews = selectInfoAndReviewsInBathroom(bathroomID)
    return HttpResponse(json.dumps(infoAndReviews))

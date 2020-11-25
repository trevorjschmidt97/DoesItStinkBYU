from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import insertRating

def indexPageView(request, bathroomID, userID, rating):
    resultString = insertRating(bathroomID, userID, rating)
    return HttpResponse("{\"result\": {\"resultString\":\"" + resultString + "\"} }")

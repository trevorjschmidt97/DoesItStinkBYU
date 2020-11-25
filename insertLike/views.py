from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import insertLike

def indexPageView(request, ratingID, userID):
    resultString = insertLike(ratingID, userID)
    return HttpResponse("{\"result\": {\"resultString\":\"" + resultString + "\"} }")

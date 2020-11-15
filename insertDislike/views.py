from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import insertDislike

def indexPageView(request, ratingID, userID):
    insertDislike(ratingID, userID)
    return HttpResponse()

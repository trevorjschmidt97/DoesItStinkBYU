from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import insertLike

def indexPageView(request, ratingID, userID):
    insertLike(ratingID, userID)
    return HttpResponse()

from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import selectInfoOfBathroom
import json

def indexPageView(request, bathroomID, userID):
    info = selectInfoOfBathroom(bathroomID, userID)
    return HttpResponse("{\"info\": " + json.dumps(info.dump()) + "}")

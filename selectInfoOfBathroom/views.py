from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import selectInfoOfBathroom
import json

def indexPageView(request, bathroomID):
    info = selectInfoOfBathroom(bathroomID)
    return HttpResponse(json.dumps(info.dump()))
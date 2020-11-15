from django.shortcuts import render
from django.http import HttpResponse
from DoesItStinkBYUData import selectBathroomsInBuilding
import json

def indexPageView(request, buildingID):
    bathrooms = selectBathroomsInBuilding(buildingID)
    return HttpResponse(json.dumps([o.dump() for o in bathrooms]))

from django.urls import path
from .views import *

urlpatterns = [
    path('<str:buildingID>', indexPageView, name='selectBathroomsInBuilding'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:bathroomID>/<int:userID>', indexPageView, name='selectBathroomsInBuilding'),
]
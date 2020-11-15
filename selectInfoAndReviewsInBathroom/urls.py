from django.urls import path
from .views import *

urlpatterns = [
    path('<str:bathroomID>', indexPageView, name='selectInfoAndReviewsInBathroom'),
]
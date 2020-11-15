from django.urls import path
from .views import *

urlpatterns = [
    path('<str:bathroomID>/<str:sort>', indexPageView, name='selectReviewsInBathroom'),
]
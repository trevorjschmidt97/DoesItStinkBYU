from django.urls import path
from .views import *

urlpatterns = [
    path('<str:bathroomID>/<str:sort>/<int:userID>', indexPageView, name='selectReviewsInBathroom'),
]
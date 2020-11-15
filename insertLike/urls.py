from django.urls import path
from .views import *

urlpatterns = [
    path('<int:ratingID>/<int:userID>', indexPageView, name='insertLike'),
]
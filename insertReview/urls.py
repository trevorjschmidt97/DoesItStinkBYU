from django.urls import path
from .views import *

urlpatterns = [
    path('<str:bathroomID>/<int:userID>/<int:rating>/<str:title>/<str:comments>', indexPageView, name='insertReview'),
]
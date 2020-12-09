from django.urls import path
from .views import *

urlpatterns = [
    path('<str:time>', indexPageView, name='selectLeaders'),
]
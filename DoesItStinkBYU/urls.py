"""DoesItStinkBYU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insertDislike/', include('insertDislike.urls')),
    path('insertLike/', include('insertLike.urls')),
    path('insertRating/', include('insertRating.urls')),
    path('insertReview/', include('insertReview.urls')),
    path('selectAllBathrooms/', include('selectAllBathrooms.urls')),
    path('selectAllBuildings/', include('selectAllBuildings.urls')),
    path('selectAllDislikes/', include('selectAllDislikes.urls')),
    path('selectAllLikes/', include('selectAllLikes.urls')),
    path('selectAllRatings/', include('selectAllRatings.urls')),
    path('selectAllReviews/', include('selectAllReviews.urls')),
    path('selectBathroomsInBuilding/', include('selectBathroomsInBuilding.urls')),
    path('selectInfoOfBathroom/', include('selectInfoOfBathroom.urls')),
    path('selectReviewsInBathroom/', include('selectReviewsInBathroom.urls')),
    path('', include('home.urls')),
]

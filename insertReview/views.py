from django.http import HttpResponse
from DoesItStinkBYUData import insertReview

def indexPageView(request, bathroomID, userID, rating, title, comments):
    insertReview(bathroomID, userID, rating, title, comments)
    return HttpResponse()

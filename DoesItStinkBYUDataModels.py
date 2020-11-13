class BasicBathroom:
    def __init__(self, bathroomID, buildingID, bathroomName, bathroomNumber, floorNumber):
        self.bathroomID = bathroomID
        self.buildingID = buildingID
        self.bathroomName = bathroomName
        self.bathroomNumber = bathroomNumber
        self.floorNumber = floorNumber
        
class BasicReview:
    def __init__(self, ratingID, title, comments, date):
        self.ratingID = ratingID
        self.title = title
        self.comments = comments
        self.date = date

class User:
    def __init__(self, userID, login, password, email):
        self.userID = userID
        self.login = login
        self.password = password
        self.email = email

class Building:
    def __init__(self, buildingID, fullBuildingName, buildingLocationLat, buildingLocationLong):
        self.buildingID = buildingID
        self.fullBuildingName = fullBuildingName
        self.buildingLocationLat = buildingLocationLat
        self.buildingLocationLong = buildingLocationLong

class Bathroom:
    def __init__(self, buildingID, bathroomName, bathroomNumber, floorNumber, numReviews, avgRating, ratings):
        self.buildingID = buildingID
        self.bathroomName = bathroomName
        self.bathroomNumber = bathroomNumber
        self.floorNumber = floorNumber
        self.numReviews = numReviews
        self.avgRating = avgRating
        self.ratings = ratings #<= is a list of number of 5, 4, 3, 2, and 1 star ratings in that order

class Review:
    def __init__(self, title, comments, date, rating, login, upvotes):
        self.title = title
        self.comments = comments
        self.date = date
        self.rating = rating
        self.login = login
        self.upvotes = upvotes


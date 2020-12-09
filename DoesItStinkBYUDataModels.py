class BasicBathroom:
    def __init__(self, bathroomID, buildingID, bathroomName, bathroomNumber, floorNumber):
        self.bathroomID = bathroomID
        self.buildingID = buildingID
        self.bathroomName = bathroomName
        self.bathroomNumber = bathroomNumber
        self.floorNumber = floorNumber
    def dump(self):
        return {'bathroomID': self.bathroomID,
                'buildingID': self.buildingID,
                'bathroomName': self.bathroomName,
                'bathroomNumber': self.bathroomNumber,
                'floorNumber': self.floorNumber}
        
class BasicReview:
    def __init__(self, ratingID, title, comments, date):
        self.ratingID = ratingID
        self.title = title
        self.comments = comments
        self.date = date
    def dump(self):
        return {'ratingID': self.ratingID,
                'title': self.title,
                'comments': self.comments,
                'date': self.date}
                            
class BasicRating:
    def __init__(self, ratingID, bathroomID, userID, rating):
        self.ratingID = ratingID
        self.bathroomID = bathroomID
        self.userID = userID
        self.rating = rating
    def dump(self):
        return {'ratingID': self.ratingID,
                'bathroomID': self.bathroomID,
                'userID': self.userID,
                'rating': self.rating}

class BasicLike:
    def __init__(self, ratingID, userID):
        self.ratingID = ratingID
        self.userID = userID
    def dump(self):
        return {'ratingID': self.ratingID,
                'userID': self.userID}

class BasicDislike:
    def __init__(self, ratingID, userID):
        self.ratingID = ratingID
        self.userID = userID
    def dump(self):
        return {'ratingID': self.ratingID,
                'userID': self.userID}

class User:
    def __init__(self, userID, login, password, email):
        self.userID = userID
        self.login = login
        self.password = password
        self.email = email
    def dump(self):
        return {'userID': self.userID,
                'login': self.login,
                'password': self.password,
                'email': self.email}

class Building:
    def __init__(self, buildingID, fullBuildingName, buildingLocationLat, buildingLocationLong):
        self.buildingID = buildingID
        self.fullBuildingName = fullBuildingName
        self.buildingLocationLat = buildingLocationLat
        self.buildingLocationLong = buildingLocationLong
    def dump(self):
        return {'buildingID': self.buildingID,
                'fullBuildingName': self.fullBuildingName,
                'buildingLocationLat': self.buildingLocationLat,
                'buildingLocationLong': self.buildingLocationLong}

class Bathroom:
    def __init__(self, buildingID, bathroomName, bathroomNumber, floorNumber, numReviews, avgRating):
        self.buildingID = buildingID
        self.bathroomName = bathroomName
        self.bathroomNumber = bathroomNumber
        self.floorNumber = floorNumber
        self.numReviews = numReviews
        self.avgRating = avgRating
        
    def dump(self):
        return {'buildingID': self.buildingID,
                'bathroomName': self.bathroomName,
                'bathroomNumber': self.bathroomNumber,
                'floorNumber': self.floorNumber,
                'numReviews': self.numReviews,
                'avgRating': self.avgRating}

class Info: 
    def __init__(self, buildingID, bathroomName, bathroomNumber, numReviews, avgRating, ratings, userRating):
        self.buildingID = buildingID
        self.bathroomName = bathroomName
        self.bathroomNumber = bathroomNumber
        self.numReviews = numReviews
        self.avgRating = avgRating
        self.num5Reviews = ratings[0]
        self.num4Reviews = ratings[1]
        self.num3Reviews = ratings[2]
        self.num2Reviews = ratings[3]
        self.num1Reviews = ratings[4]
        self.userRating = userRating

    def dump(self):
        return {'buildingID': self.buildingID,
                'bathroomName': self.bathroomName,
                'bathroomNumber': self.bathroomNumber,
                'numReviews': self.numReviews,
                'avgRating': self.avgRating,
                'num5Reviews': self.num5Reviews,
                'num4Reviews': self.num4Reviews,
                'num3Reviews': self.num3Reviews,
                'num2Reviews': self.num2Reviews,
                'num1Reviews': self.num1Reviews,
                'userRating': self.userRating}

class Review:
    def __init__(self, ratingID, title, comments, date, rating, login, upvotes, userLiked, userDisliked):
        self.ratingID = ratingID
        self.title = title
        self.comments = comments
        self.date = date
        self.rating = rating
        self.login = login
        self.upvotes = upvotes
        self.userLiked = userLiked
        self.userDisliked = userDisliked
    def dump(self):
        return {'ratingID': self.ratingID,
                'title': self.title,
                'comments': self.comments,
                'date': self.date,
                'rating': self.rating,
                'login': self.login,
                'upvotes': self.upvotes,
                'userLiked': self.userLiked,
                'userDisliked': self.userDisliked}

class Leader:
    def __init__(self, username, upvotes):
        self.username = username
        self.upvotes = upvotes
    def dump(self):
        return {'username': self.username,
                'upvotes': self.upvotes}
    def __str__(self) -> str:
        return str(self.username) + " " + str(self.upvotes)




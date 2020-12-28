from DoesItStinkBYUDataModels import *
# For debugging/fakedata
def selectAllUsers():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = """SELECT * FROM User;"""

        cursor.execute(sql)

        rows = cursor.fetchall()

        users = []
        for row in rows:
            user = User(row[0],row[1],row[2],row[3])
            users.append(user)

        conn.commit()
        cursor.close()
        ret = users
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        ret = None
    finally:
        if (conn):
            conn.close()

    return ret
def selectAllBathrooms():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "SELECT * FROM Bathroom"

        cursor.execute(sql)

        rows = cursor.fetchall()

        bathrooms = []
        for row in rows:
            
            bathroom = BasicBathroom(row[0], row[1], row[2], row[3], row[4])
            bathrooms.append(bathroom)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
        return bathrooms
def selectAllReviews():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "SELECT * FROM Review"

        cursor.execute(sql)

        rows = cursor.fetchall()

        reviews = []
        for row in rows:
            
            review = BasicReview(row[0], row[1], row[2], row[3])
            reviews.append(review)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
        return reviews
def selectAllRatings():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "SELECT * FROM Rating"

        cursor.execute(sql)

        rows = cursor.fetchall()

        ratings = []
        for row in rows:
            rating = BasicRating(row[0], row[1], row[2], row[3])
            ratings.append(rating)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
        return ratings
def selectAllLikes():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "SELECT * FROM Like"

        cursor.execute(sql)

        rows = cursor.fetchall()

        likes = []
        for row in rows:
            like = BasicLike(row[0], row[1])
            likes.append(like)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
        return likes
def selectAllDislikes():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "SELECT * FROM Dislike"

        cursor.execute(sql)

        rows = cursor.fetchall()

        dislikes = []
        for row in rows:
            dislike = BasicDislike(row[0], row[1])
            dislikes.append(dislike)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
        return dislikes

def deleteReview(bathroomID, userID):
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sqlSelect = """SELECT ratingID FROM Rating
        WHERE bathroomID = '""" + bathroomID + """' AND userID = """ + str(userID) + """;"""
        cursor.execute(sqlSelect)

        ratingID = cursor.fetchone()[0]

        sqlDelete = """DELETE FROM Review
        WHERE ratingID = """ + str(ratingID) + """;"""

        cursor.execute(sqlDelete)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
# deleteReview('mlbm2008', 103)

def deleteAllLikes():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "DELETE FROM Like"

        cursor.execute(sql)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
def deleteAllDislikes():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "DELETE FROM Dislike"

        cursor.execute(sql)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
def deleteAllReviews():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "DELETE FROM Review"

        cursor.execute(sql)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
def deleteAllRatings():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "DELETE FROM Rating"

        cursor.execute(sql)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
def deleteAllBathrooms():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "DELETE FROM Bathroom"

        cursor.execute(sql)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
def deleteAllBuildings():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "DELETE FROM Building"

        cursor.execute(sql)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
def deleteAllUsers():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = "DELETE FROM User"

        cursor.execute(sql)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
def deleteAllData():
    deleteAllLikes()
    deleteAllDislikes()
    deleteAllReviews()
    deleteAllRatings()
    deleteAllBathrooms()
    deleteAllBuildings()
    deleteAllUsers()
def deleteAllNonEssentialData():
    deleteAllLikes()
    deleteAllDislikes()
    deleteAllReviews()
    deleteAllRatings()
    #deleteAllBathrooms()
    #deleteAllBuildings()
    deleteAllUsers()
def insertUser(login, password, email):
    import sqlite3
    success = True
    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        # check to see if the login exists
        sqlSelect = """SELECT * FROM User
        WHERE login = '""" + login + """';"""
        cursor.execute(sqlSelect)

        if len(cursor.fetchall()) == 0:
            insert = """INSERT INTO User 
            (login, password, email) 
            VALUES (?,?,?);"""
            dataTuple = (login, password, email)

            cursor.execute(insert, dataTuple)
        else:
            success = False

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table:", error)
    finally:
        if (conn):
            conn.close()
    if not success:
        return 'Error occured, login already taken, select new'
# print(insertUser('holyschmidtty', 'ThisIsMyPassword', 'trevorjschmidt97@gmail.com'))

# Returns all buildings in an list of Building Objects
def selectAllBuildings():
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sql = """SELECT buildingID, fullBuildingName, buildingLocationLat, buildingLocationLong
                 FROM Building;"""

        cursor.execute(sql)

        rows = cursor.fetchall()

        buildings = []
        for row in rows:
            building = Building(row[0],row[1],row[2],row[3])
            buildings.append(building)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
        return buildings
# buildings = selectAllBuildings()
# print('Total number of buildings:', len(buildings))
# for building in buildings:
#     print(building.buildingID, building.fullBuildingName, building.buildingLocationLat, building.buildingLocationLong)

# Takes a buildingID, gives a list of Bathrooms with Info in a list of Bathroom Objects
def selectBathroomsInBuilding(buildingID):
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        buildingID = "'" + buildingID + "'"

        sql = """SELECT buildingID, bathroomName, bathroomNumber, floorNumber,
                 (SELECT COUNT(*) AS Exp1 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID) AS numReviews,
                 (SELECT AVG(Rating.rating) AS Exp2 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID) AS avgRating
                 FROM Bathroom
                 WHERE buildingID = """ + buildingID + """
                 ORDER BY floorNumber, bathroomNumber ASC;"""
        cursor.execute(sql)

        rows = cursor.fetchall()

        bathrooms = []
        for row in rows:
            bathroom = Bathroom(row[0], row[1], row[2], row[3], row[4], row[5])
            bathrooms.append(bathroom)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
        return bathrooms
# bathrooms = selectBathroomsInBuilding('UPC')
# for bathroom in bathrooms:
#     print(bathroom.buildingID, bathroom.bathroomName, bathroom.bathroomNumber, bathroom.floorNumber, '\t', bathroom.numReviews, bathroom.avgRating)

# Takes a bathroomID, and sort, 0=>newest, 1=> oldest, 2=>highestRating, 3=>lowestRating gives a list of Review objects
def selectInfoOfBathroom(bathroomID, userID):
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sqlSelectBathroomInfo = """SELECT buildingID, bathroomName, bathroomNumber,
        (SELECT COUNT(*) AS Exp1 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID) AS numReviews,
        (SELECT AVG(Rating.rating) AS Exp2 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID) AS avgRating,
        (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 5) AS numFiveReviews,
        (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 4) AS numFourReviews,
        (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 3) AS numThreeReviews,
        (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 2) AS numTwoReviews,
        (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 1) AS numOneReviews,
        (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = '""" + bathroomID + """' AND Rating.userID = '""" + str(userID) + """') AS userRating
        FROM Bathroom
        WHERE bathroomID = '""" + bathroomID + """'
        ;"""
        cursor.execute(sqlSelectBathroomInfo)

        data = cursor.fetchone()
        if data[10] == 1:
            sqlSelectRatingOfBathroom = """SELECT rating
                                           FROM Rating
                                           WHERE bathroomID = '""" + bathroomID + """' AND Rating.userID = '""" + str(userID) + """'
                                           """
            cursor.execute(sqlSelectRatingOfBathroom)
            rating = cursor.fetchone()[0]
        else:
            rating = 0

        ratings = [data[5], data[6], data[7], data[8], data[9]]
        info = Info(data[0], data[1], data[2], data[3], data[4], ratings, rating)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
    return info
# info = selectInfoOfBathroom('moa372A', 153)
# print(info.userRating)

# Takes a bathroom, and sort, gives a list of Review objects
def selectReviewsInBathroom(bathroomID, sort, userID):
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        order = ''

        if sort == 'newest':
            order = 'Review.date DESC'
        elif sort == 'oldest':
            order = 'Review.date ASC'
        elif sort == 'highestRating':
            order = 'Upvotes DESC'
        elif sort == 'lowestRating':
            order = 'Upvotes ASC'


        sql = """SELECT Review.ratingID, title, comments, date, Rating.rating, User.login,
        (SELECT COUNT(*) AS Exp1 FROM Like WHERE Review.ratingID = Like.ratingID) 
            - (SELECT COUNT(*) AS Exp2 FROM Dislike WHERE Review.ratingID = Dislike.ratingID) AS Upvotes,
        (SELECT COUNT(*) AS Exp2 FROM Like WHERE Review.ratingID = Like.ratingID AND Like.userID = '""" + str(userID) + """') AS userLiked,
        (SELECT COUNT(*) AS Exp2 FROM Dislike WHERE Review.ratingID = Dislike.ratingID AND Dislike.userID = '""" + str(userID) + """') AS userDisliked
        FROM Review
        INNER JOIN Rating ON Review.ratingID = Rating.ratingID
        INNER JOIN User ON Rating.userID = User.userID
        WHERE Rating.bathroomID = '""" + bathroomID + """'
        ORDER BY """ + order + """
        ;"""

        cursor.execute(sql)

        rows = cursor.fetchall()
        reviews = []
        for row in rows:
            review = Review(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            reviews.append(review)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
        return reviews
# reviews = selectReviewsInBathroom('rb2207', 'lowestRating', 152)
# for review in reviews:
#     print(review.date, review.upvotes, review.title, review.comments, review.rating, review.login, '\n', review.userLiked, review.userDisliked)

def selectLeaders(time='allTime'):
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        day = """
                 SELECT User.login, (tbl1.NumLikes - tbl2.NumDislikes) AS Upvotes
                 FROM User
                 INNER JOIN
                 (
                 SELECT User.userID, COUNT(*) AS NumLikes
                 FROM User
                 INNER JOIN Rating ON User.userID = Rating.userID
                 INNER JOIN Review ON Rating.ratingID = Review.ratingID
                 INNER JOIN Like ON Review.ratingID = Like.ratingID
                 WHERE strftime('%j', date('now')) = strftime('%j', Review.date)
                   AND strftime('%Y', date('now')) = strftime('%Y', Review.date)
                 GROUP BY User.userID
                 ) AS tbl1 ON User.userID = tbl1.userID
                 INNER JOIN
                 (
                 SELECT User.userID, COUNT(*) AS NumDislikes
                 FROM User
                 INNER JOIN Rating ON User.userID = Rating.userID
                 INNER JOIN Review ON Rating.ratingID = Review.ratingID
                 INNER JOIN Dislike ON Review.ratingID = Dislike.ratingID
                 WHERE strftime('%j', date('now')) = strftime('%j', Review.date)
                 GROUP BY User.userID
                 ) AS tbl2 ON User.userID = tbl2.userID
                 ORDER BY (tbl1.NumLikes - tbl2.NumDislikes) DESC
                 LIMIT 20;
                 """

        week = """
                 SELECT User.login, (tbl1.NumLikes - tbl2.NumDislikes) AS Upvotes
                 FROM User
                 INNER JOIN
                 (
                 SELECT User.userID, COUNT(*) AS NumLikes
                 FROM User
                 INNER JOIN Rating ON User.userID = Rating.userID
                 INNER JOIN Review ON Rating.ratingID = Review.ratingID
                 INNER JOIN Like ON Review.ratingID = Like.ratingID
                 WHERE strftime('%W', date('now')) = strftime('%W', Review.date)
                   AND strftime('%Y', date('now')) = strftime('%Y', Review.date)
                 GROUP BY User.userID
                 ) AS tbl1 ON User.userID = tbl1.userID
                 INNER JOIN
                 (
                 SELECT User.userID, COUNT(*) AS NumDislikes
                 FROM User
                 INNER JOIN Rating ON User.userID = Rating.userID
                 INNER JOIN Review ON Rating.ratingID = Review.ratingID
                 INNER JOIN Dislike ON Review.ratingID = Dislike.ratingID
                 WHERE strftime('%W', date('now')) = strftime('%W', Review.date)
                   AND strftime('%Y', date('now')) = strftime('%Y', Review.date)
                 GROUP BY User.userID
                 ) AS tbl2 ON User.userID = tbl2.userID
                 ORDER BY (tbl1.NumLikes - tbl2.NumDislikes) DESC
                 LIMIT 20;
                 """

        month = """
                 SELECT User.login, (tbl1.NumLikes - tbl2.NumDislikes) AS Upvotes
                 FROM User
                 INNER JOIN
                 (
                 SELECT User.userID, COUNT(*) AS NumLikes
                 FROM User
                 INNER JOIN Rating ON User.userID = Rating.userID
                 INNER JOIN Review ON Rating.ratingID = Review.ratingID
                 INNER JOIN Like ON Review.ratingID = Like.ratingID
                 WHERE strftime('%m', date('now')) = strftime('%m', Review.date)
                   AND strftime('%Y', date('now')) = strftime('%Y', Review.date)
                 GROUP BY User.userID
                 ) AS tbl1 ON User.userID = tbl1.userID
                 INNER JOIN
                 (
                 SELECT User.userID, COUNT(*) AS NumDislikes
                 FROM User
                 INNER JOIN Rating ON User.userID = Rating.userID
                 INNER JOIN Review ON Rating.ratingID = Review.ratingID
                 INNER JOIN Dislike ON Review.ratingID = Dislike.ratingID
                 WHERE strftime('%m', date('now')) = strftime('%m', Review.date)
                   AND strftime('%Y', date('now')) = strftime('%Y', Review.date)
                 GROUP BY User.userID
                 ) AS tbl2 ON User.userID = tbl2.userID
                 ORDER BY (tbl1.NumLikes - tbl2.NumDislikes) DESC
                 LIMIT 20;
                 """

        allTime = """
                 SELECT User.login, (tbl1.NumLikes - tbl2.NumDislikes) AS Upvotes
                 FROM User
                 INNER JOIN
                 (
                 SELECT User.userID, COUNT(*) AS NumLikes
                 FROM User
                 INNER JOIN Rating ON User.userID = Rating.userID
                 INNER JOIN Review ON Rating.ratingID = Review.ratingID
                 INNER JOIN Like ON Review.ratingID = Like.ratingID
                 GROUP BY User.userID
                 ) AS tbl1 ON User.userID = tbl1.userID
                 INNER JOIN
                 (
                 SELECT User.userID, COUNT(*) AS NumDislikes
                 FROM User
                 INNER JOIN Rating ON User.userID = Rating.userID
                 INNER JOIN Review ON Rating.ratingID = Review.ratingID
                 INNER JOIN Dislike ON Review.ratingID = Dislike.ratingID
                 GROUP BY User.userID
                 ) AS tbl2 ON User.userID = tbl2.userID
                 ORDER BY (tbl1.NumLikes - tbl2.NumDislikes) DESC
                 LIMIT 20;
                 """
        if time == 'day':
            cursor.execute(day)
        elif time == 'week':
            cursor.execute(week)
        elif time == 'month':
            cursor.execute(month)
        else:
            cursor.execute(allTime)

        leaders = []
        rows = cursor.fetchall()
        if len(rows) == 0:
            newLeader = Leader("Currently no reviews for this time period", 69)
            leaders.append(newLeader)
        else:
            for row in rows:
                newLeader = Leader(row[0], row[1])
                leaders.append(newLeader)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
            return leaders
# for i, leader in enumerate(getLeaderBoards('week')):
#     print(i, ":", leader)

# Allows a user to leave a rating, will update rating if user already has one
def insertRating(bathroomID, userID, rating):
    import sqlite3

    returnString = ""

    # If user already has a rating for that bathroom, only update,
    # else insert
    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sqlInsert = """INSERT INTO Rating
        (bathroomID, userID, rating)
        VALUES (?,?,?);"""
        dataTuple = (bathroomID, userID, rating)

        bathroomID = "'" + bathroomID + "'"
        userID = "'" + str(userID) + "'"
        rating = str(rating)

        sqlSelect = """SELECT * FROM Rating
        WHERE bathroomID = """ + bathroomID + """ AND userID = """ + userID

        sqlUpdate = """UPDATE Rating
        SET rating = """ + rating + """
        WHERE bathroomID = """ + bathroomID + """ AND userID = """ + userID

        cursor.execute(sqlSelect)
        ratings = cursor.fetchall()

        if len(ratings) > 0:
            returnString = "Rating updated"
            # Then update
            cursor.execute(sqlUpdate)
        else:
            # Simply insert
            returnString = "Rating inserted"
            cursor.execute(sqlInsert, dataTuple)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return "Failed to work with insertion of rating into db"
    finally:
        if (conn):
            conn.close()
            return returnString
#insertRating('rb161L', 54, 2)

# Allows a user to like a review, will delete dislike if exists, also may delete like if already exists
def insertLike(ratingID, userID):
    import sqlite3

    returnString = ""

    # CASE 1: User hasn't liked nor disliked the review => Insert like
    # CASE 2: User has liked the review, so liking again will delete the like => Delete Like
    # CASE 3: User has disliked the review, so liking will also delete the dislike => Delete Dislike, Insert like
    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sqlSelectLikes = """SELECT * FROM Like
        WHERE ratingID = """ + str(ratingID) + """ and userID = """ + str(userID)
        cursor.execute(sqlSelectLikes)
        likes = cursor.fetchall()

        sqlSelectDislikes = """SELECT * FROM Dislike
        WHERE ratingID = """ + str(ratingID) + """ and userID = """ + str(userID)
        cursor.execute(sqlSelectDislikes)
        dislikes = cursor.fetchall()

        sqlInsertLike = """INSERT INTO Like (ratingID, userID)
        VALUES (?,?);"""
        insertLikeDataTuple = (ratingID, userID)

        sqlDeleteLike = """DELETE FROM Like
        WHERE ratingID = """ + str(ratingID) + """ and userID = """ + str(userID)

        sqlDeleteDislike = """DELETE FROM Dislike
        WHERE ratingID = """ + str(ratingID) + """ and userID = """ + str(userID)

        if len(likes) == 0 and len(dislikes) == 0:
            #CASE 1
            returnString = "Like inserted"
            cursor.execute(sqlInsertLike, insertLikeDataTuple)
        elif len(likes) != 0 and len(dislikes) == 0:
            returnString = "Like deleted"
            cursor.execute(sqlDeleteLike)
        elif len(likes) == 0 and len(dislikes) != 0:
            returnString = "Dislike deleted, like inserted"
            cursor.execute(sqlDeleteDislike)
            cursor.execute(sqlInsertLike,insertLikeDataTuple)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return "Failed to insert like into db"
    finally:
        if (conn):
            conn.close()
            return returnString
#insertLike(2019, 53)

# Allows a user to dislike a review, will delete like if exists, also may delete dislike if already exists
def insertDislike(ratingID, userID):
    import sqlite3

    returnString = ""

    # CASE 1: User hasn't liked nor disliked the review => Insert Dislike
    # CASE 2: User has disliked the review => Delete Dislike
    # CASE 3: User has liked the review => Delete Like, Insert Dislike
    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        sqlSelectLikes = """SELECT * FROM Like
        WHERE ratingID = """ + str(ratingID) + """ and userID = """ + str(userID)
        cursor.execute(sqlSelectLikes)
        likes = cursor.fetchall()

        sqlSelectDislikes = """SELECT * FROM Dislike
        WHERE ratingID = """ + str(ratingID) + """ and userID = """ + str(userID)
        cursor.execute(sqlSelectDislikes)
        dislikes = cursor.fetchall()

        sqlInsertDislike = """INSERT INTO Dislike (ratingID, userID)
        VALUES (?,?);"""
        insertDislikeDataTuple = (ratingID, userID)

        sqlDeleteLike = """DELETE FROM Like
        WHERE ratingID = """ + str(ratingID) + """ and userID = """ + str(userID)

        sqlDeleteDislike = """DELETE FROM Dislike
        WHERE ratingID = """ + str(ratingID) + """ and userID = """ + str(userID)

        if len(likes) == 0 and len(dislikes) == 0:
            #CASE 1
            returnString = "Dislike inserted"
            cursor.execute(sqlInsertDislike, insertDislikeDataTuple)

        elif len(likes) == 0 and len(dislikes) != 0:
            #case 2
            returnString = "Dislike deleted"
            cursor.execute(sqlDeleteDislike)
        elif len(likes) != 0 and len(dislikes) == 0:
            #case 3
            returnString = "Like deleted, dislike inserted"
            cursor.execute(sqlDeleteLike)
            cursor.execute(sqlInsertDislike, insertDislikeDataTuple)
        

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return "Error pushing dislike to db"
    finally:
        if (conn):
            conn.close()
            return returnString
# insertDislike(2019, 54)

# Allows a user to leave a review, will update rating and/or review if already exists
def insertReview(bathroomID, userID, rating, title, comments):
    import sqlite3
    from datetime import datetime
    title = title.replace("insertSpace", " ")
    title = title.replace("insertAsterisk", "'")
    title = title.replace("insertForwardSlash", "/")
    title = title.replace("insertBackSlash", "\\")
    title = title.replace("insertPercent", "%")
    title = title.replace("insertNewLine", "\\n")
    comments = comments.replace("insertSpace", " ")
    comments = comments.replace("insertAsterisk", "'")
    comments = comments.replace("insertForwardSlash", "/")
    comments = comments.replace("insertBackSlash", "\\")
    comments = comments.replace("insertPercent", "%")
    comments = comments.replace("insertNewLine", "\\n")
    if comments == "No comment":
        comments = ""
    returnString = ""

    # Case 1: User doesn't have a rating, nor a review
    # Case 2: User has a rating, but not a review
    # Case 3: User has a rating, and a review

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        bathroomIDEdit = "'" + bathroomID + "'"
        userIDEdit = "'" + str(userID) + "'"
        ratingEdit = str(rating)

        # Check if there's a rating
        sqlSelect = """SELECT * FROM Rating
        WHERE bathroomID = """ + bathroomIDEdit + """ AND userID = """ + userIDEdit

        cursor.execute(sqlSelect)
        ratings = None
        ratings = cursor.fetchall()

        # Case 1:
        if len(ratings) == 0: # User doesn't have a rating
            returnString = "Rating and Review inserted"
            # Insert rating
            sqlInsertRating = """INSERT INTO Rating
            (bathroomID, userID, rating)
            VALUES (?,?,?);"""
            dataTupleRating = (bathroomID, userID, rating)
            
            cursor.execute(sqlInsertRating, dataTupleRating)

            # Then grab that ratingID
            sqlSelect = """SELECT * FROM Rating
            WHERE bathroomID = """ + bathroomIDEdit + """ AND userID = """ + userIDEdit

            cursor.execute(sqlSelect)
            ratings = None
            ratings = cursor.fetchall()

            # And insert into review
            sqlInsertReview = """INSERT INTO Review
            (ratingID, title, comments, date)
            VALUES (?,?,?,?);"""
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            dataTupleReview = (ratings[0][0], title, comments, formatted_date)
            cursor.execute(sqlInsertReview, dataTupleReview)
        else: #Case 2/3:
            returnString = "Rating updated"
            # Update rating
            sqlUpdate = """UPDATE Rating
            SET rating = """ + ratingEdit + """
            WHERE bathroomID = """ + bathroomIDEdit + """ AND userID = """ + userIDEdit
            cursor.execute(sqlUpdate)

            #Now check for a review
            sqlSelectReview = """SELECT * FROM Review
            WHERE ratingID = """ + str(ratings[0][0])
            cursor.execute(sqlSelectReview)
            reviews = cursor.fetchall()

            # Case 2
            if len(reviews) != 0: # User had a review
                returnString += " and review updated"
                # Delete Review
                sqlUpdateReview = """DELETE FROM Review
                WHERE ratingID = """ + str(ratings[0][0])
                cursor.execute(sqlUpdateReview)
            else:
                returnString += " and review inserted"

            # Then Insert review
            sqlInsertReview = """INSERT INTO Review
            (ratingID, title, comments, date)
            VALUES (?,?,?,?);"""
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            dataTupleReview = (ratings[0][0], title, comments, formatted_date)
            cursor.execute(sqlInsertReview, dataTupleReview)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return "Failed to insert review into db"
    finally:
        if (conn):
            conn.close()
            return returnString
# insertReview('rb161L', 55, 4, 'Great Bathroom', 'I really enjoyed using this bathroom a lot.')

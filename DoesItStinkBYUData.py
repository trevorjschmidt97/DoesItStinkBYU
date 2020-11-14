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

        sql = """SELECT * FROM Building;"""

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
                 (SELECT AVG(Rating.rating) AS Exp2 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID) AS avgRating,
                 (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 5) AS numFiveReviews,
                 (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 4) AS numFourReviews,
                 (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 3) AS numThreeReviews,
                 (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 2) AS numTwoReviews,
                 (SELECT COUNT(*) AS Exp3 FROM Rating WHERE Rating.bathroomID = Bathroom.bathroomID AND Rating.rating = 1) AS numOneReviews
                 FROM Bathroom
                 WHERE buildingID = """ + buildingID + """
                 ORDER BY floorNumber, bathroomNumber ASC;"""

        cursor.execute(sql)

        rows = cursor.fetchall()

        bathrooms = []
        for row in rows:
            ratings = [row[6], row[7], row[8], row[9], row[10]]
            bathroom = Bathroom(row[0], row[1], row[2], row[3], row[4], row[5], ratings)
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
#     print(bathroom.buildingID, bathroom.bathroomName, bathroom.bathroomNumber, bathroom.floorNumber, '\t', bathroom.numReviews, bathroom.avgRating, bathroom.ratings)

# Takes a bathroom, gives a list of Review objects
def selectReviewsInBathroom(bathroomID, highestRated=False, lowestRated=False, newest=False, oldest=False):
    import sqlite3

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        order = ''

        if newest:
            order = 'Review.date DESC'
        elif oldest:
            order = 'Review.date ASC'
        elif highestRated:
            order = 'Upvotes DESC'
        elif lowestRated:
            order = 'Upvotes ASC'


        sql = """SELECT title, comments, date, Rating.rating, User.login,
        (SELECT COUNT(*) AS Exp1 FROM Like WHERE Review.ratingID = Like.ratingID) 
            - (SELECT COUNT(*) AS Exp2 FROM Dislike WHERE Review.ratingID = Dislike.ratingID) AS Upvotes
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
            review = Review(row[0], row[1], row[2], row[3], row[4], row[5])
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
# reviews = selectReviewsInBathroom('lvesW105C', oldest=True)
# for review in reviews:
#     print(review.date, review.upvotes, review.title, review.comments, review.rating, review.login)

# Allows a user to leave a rating, will update rating if user already has one
def insertRating(bathroomID, userID, rating):
    import sqlite3

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
            # Then update
            cursor.execute(sqlUpdate)
        else:
            # Simply insert
            cursor.execute(sqlInsert, dataTuple)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
#insertRating('rb161L', 54, 2)

# Allows a user to leave a review, will update rating and/or review if already exists
def insertReview(bathroomID, userID, rating, title, comments):
    import sqlite3
    from datetime import datetime

    # Case 1: User doesn't have a rating, nor a review
    # Case 2: User has a rating, but not a review
    # Case 3: User has a rating, and a review

    try:
        conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
        cursor = conn.cursor()

        bathroomIDEdit = "'" + bathroomID + "'"
        userIDEdit = "'" + str(userID) + "'"
        ratingEdit = str(rating)
        titleEdit = "'" + title + "'"
        commentsEdit = "'" + comments + "'"

        # Check if there's a rating
        sqlSelect = """SELECT * FROM Rating
        WHERE bathroomID = """ + bathroomIDEdit + """ AND userID = """ + userIDEdit

        cursor.execute(sqlSelect)
        ratings = None
        ratings = cursor.fetchall()

        # Case 1:
        if len(ratings) == 0: # User doesn't have a rating
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
                # Delete Review
                sqlUpdateReview = """DELETE FROM Review
                WHERE ratingID = """ + str(ratings[0][0])
                cursor.execute(sqlUpdateReview)

            # Then Insert review
            sqlInsertReview = """INSERT INTO Review
            (ratingID, title, comments, date)
            VALUES (?,?,?,?);"""
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            dataTupleReview = (ratings[0][0], title, comments,formatted_date)
            cursor.execute(sqlInsertReview, dataTupleReview)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
    finally:
        if (conn):
            conn.close()
# insertReview('rb161L', 55, 4, 'Great Bathroom', 'I really enjoyed using this bathroom a lot.')

# Allows a user to like a review, will delete dislike if exists, also may delete like if already exists
def insertLike(ratingID, userID):
    import sqlite3

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
            cursor.execute(sqlInsertLike, insertLikeDataTuple)
        elif len(likes) != 0 and len(dislikes) == 0:
            cursor.execute(sqlDeleteLike)
        elif len(likes) == 0 and len(dislikes) != 0:
            cursor.execute(sqlDeleteDislike)
            cursor.execute(sqlInsertLike,insertLikeDataTuple)

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
#insertLike(2019, 53)

# Allows a user to dislike a review, will delete like if exists, also may delete dislike if already exists
def insertDislike(ratingID, userID):
    import sqlite3

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
            cursor.execute(sqlInsertDislike, insertDislikeDataTuple)
        elif len(likes) == 0 and len(dislikes) != 0:
            #case 2
            cursor.execute(sqlDeleteDislike)
        elif len(likes) != 0 and len(dislikes) == 0:
            #case 3
            cursor.execute(sqlDeleteLike)
            cursor.execute(sqlInsertDislike, insertDislikeDataTuple)
        

        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to work with database:", error)
        return None
    finally:
        if (conn):
            conn.close()
# insertDislike(2019, 54)

import model
import csv
from datetime import datetime

def load_users(session):
    # use u.user
    with open('seed_data/u.user', 'rb') as csvfile:
        userreader = csv.reader(csvfile, delimiter = "|")
        for row in userreader:
            user = model.User(email=" ", password=" ", age=row[1], zipcode=row[4])
            session.add(user)
    session.commit()


def load_movies(session):
    # use u.item
    with open('seed_data/u.item', 'rb') as csvfile:
        userreader = csv.reader(csvfile, delimiter = "|")
        for row in userreader:
            movie_title = row[1]
            movie_title = movie_title.decode("latin-1")
            movie_title = movie_title.strip(movie_title[-7:len(movie_title)])
            date = row[2]
            if date:
                date = datetime.strptime(date, "%d-%b-%Y")
                movie = model.Movie(title=movie_title, release_date=date, imdb_url=row[4])
                session.add(movie)
            else:
                movie = model.Movie(title=movie_title, imdb_url=row[4])
    session.commit()


def load_ratings(session):
    # use u.data
    f = open ("seed_data/u.data")       
    for row in f:
        data = row.strip().split("\t")
        data = model.Rating(user_id=data[0], movie_id=data[1], rating=data[2])
        session.add(data)
    session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    # load_users(session)
    load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)

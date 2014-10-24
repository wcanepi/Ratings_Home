import model
import csv

def load_users(session):
    # use u.user
    with open('seed_data/shortuser.csv', 'rb') as csvfile:
        userreader = csv.reader(csvfile, delimiter = "|", quotechar='|')
        for row in userreader:
            user = model.User(email=" ", password=" ", age=row[1], zipcode=row[4])
            session.add(user)
            session.commit()


def load_movies(session):
    # use u.item
    with open('seed_data/shortitem.csv', 'rb') as csvfile:
        userreader = csv.reader(csvfile, delimiter = "|", quotechar='|')
        for row in userreader:
            movie_title = row[1]
            movie_title = movie_title.strip(movie_title[-6:len(movie_title)])
            print movie_title
            #movie = model.Movies(title=row[1], release_date=row[2], imdb_url=row[4])
            # session.add(movie)
            # session.commit()

def load_ratings(session):
    # use u.data
    with open('seed_data/shortdata.csv', 'rb') as csvfile:
        userreader = csv.reader(csvfile, delimiter = " ", quotechar='|')
        for row in userreader:
            print row
            user = model.User(email=" ", password=" ", age=row[1], zipcode=row[4])
            session.add(user)
            session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    # load_users(session)
      load_movies(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)

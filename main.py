from imdb import Cinemagoer
import sys, csv

# variables
MOVIE_COUNT = 0
directors = {}
actors = {}

# get the file name
fileName = sys.argv[1]


# create an instance of the Cinemagoer class
ia = Cinemagoer()

# parse CSV file

file = open(fileName, 'r')

try:
    reader = csv.reader(file)
    next(file)
    for row in reader:
        movie_name = row[1]

        imdb_movie = ia.search_movie(movie_name)

        # test
        #assert movie_name == imdb_movieName
        print(movie_name)
        print(imdb_movie)
        #print(imdb_movie)

        # add 1 to counter
        MOVIE_COUNT += 1











finally:
    file.close()
    print("Total Number of movies watched is", MOVIE_COUNT)

from imdb import Cinemagoer
import sys, csv

# variables
MOVIE_COUNT = 0


# get the file name

fileName = sys.argv[1]


# create an instance of the Cinemagoer class
ia = Cinemagoer()

# parse CSV file

file = open(fileName, 'r')

try:
    reader = csv.reader(file)
    for row in reader:
        movie_name = row[1]
        # test
        print(movie_name)
        MOVIE_COUNT += 1










finally:
    file.close()
    print("Total Number of movies watched is", MOVIE_COUNT)

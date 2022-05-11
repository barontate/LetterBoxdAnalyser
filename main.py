from imdb import Cinemagoer
import sys, csv

# get the file name

fileName = sys.argv[1]

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# parse CSV file

with open(fileName, 'r') as file:
    reader = csv.reader(file)
    for each_row in reader:
        print(each_row)

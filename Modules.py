
import os
import csv

Title = input("What title are you looking for? ")
csvpath = os.path.join( "Python_Prueba", 'netflix_rating.csv')

found = False

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    

    for row in csvreader:
        if Title == row[0]:
            print(row[0] + " is rated " + Row[1] + "with a rating of " + row[5])
    
            found = True

            break

    if found is False:
        print("sorry, we dont have what you are looking for")
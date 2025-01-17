"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-14"
-------------------------------------------------------
"""
#import 
from Movie_utilities import get_by_genres, read_movies

fv = open("movies.txt", "r")
movies = read_movies(fv)

numbers = [3,4,5,8]
lister = get_by_genres(movies, numbers)

for each in lister:
    print(each)
    print()
 


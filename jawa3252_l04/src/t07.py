"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-28"
-------------------------------------------------------
"""

from Movie_utilities import read_movies
from utilities import list_test
from List_array import List

movies = List()

fh = open("movies.txt", "r", encoding="utf-8")

movie = read_movies(fh)

for each in movie:
    movies.append(each)
    
print(movies._values)
    
list_test(movies)
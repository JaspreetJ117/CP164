"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-13"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_test
from Movie_utilities import read_movie

s = Stack()

fh = open("movies.txt", "r", encoding="utf-8")
movie = []

for line in fh:
    movie.append(read_movie(line))


stack_test(movie)

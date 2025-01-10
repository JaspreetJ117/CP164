"""
-------------------------------------------------------
Testing genre_menu which prints the list of genres in the
data base
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-10"
-------------------------------------------------------
"""
from Movie import Movie

movie = Movie(
    title="Data Structures",
    year=1994,
    director="Professor Brown",
    rating=9.2,
    genres=[1, 2, 3, 4]
)

genres = movie.genres_menu()
print(genres)
 



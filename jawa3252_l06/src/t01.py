"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-02-15"
-------------------------------------------------------
"""

from List_linked import List

playlist = List()

playlist.prepend("The Godfather")
playlist.append("The Shawshank Redemption")
playlist.insert(1, "The Dark Knight")

for each in playlist:
    print(each)

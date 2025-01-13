"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-10"
-------------------------------------------------------
"""
from functions import median_scores

with open("numbers.txt", "r") as file:
    median = median_scores(file)
    print("Median:", median)
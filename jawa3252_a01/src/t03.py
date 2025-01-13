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

from functions import file_analyze

fh = open("numbers.txt", "r", encoding="utf-8")

upp, low, dig, whi, rem = file_analyze(fh)

print(f"""
Uppercase:  {upp}
Lowercase:  {low}
Digits:     {dig}
WhiteSpace: {whi}
Remaining:  {rem}
""")
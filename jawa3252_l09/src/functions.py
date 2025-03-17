"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-03-13"
-------------------------------------------------------
"""

from Movie import Movie

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash Slot Key
    --------------------------------
    1652346 3 Dark City, 1998
    848448  6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    
    
    for value in values:
    
        hsh = hash(value)
        slot = hsh % slots
        key = value.key()
        print("{:8}{:5} {}".format(hsh, slot, key))
            
    return 
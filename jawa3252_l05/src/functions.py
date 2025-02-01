"""
-------------------------------------------------------
Recursion
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-24"
-------------------------------------------------------
"""

#Constants 
VOWELS = "aeiou"

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    ans = 0
    if x < 0 or y < 0:
        ans = x - y
        
    else:
        ans = recurse(x-1,y) + recurse(x,y-1)
        
    return ans

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    ans = 0 
    
    if m%n == 0:  
        ans = n
    
    else:
        ans = gcd(n, m%n)
        
    return ans

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    
    if len(s) > 0:
        c = s[0]
        s = s[1:]
        
        if c.lower() in VOWELS:
            count = 1 + vowel_count(s)
            
        else:
            count = vowel_count(s)
            
    else:
        count = 0
        
    return count

def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    
    if power > 1:
        power -= 1
        ans = base * to_power(base, power)

    elif power < 0:
        power += 1 
        ans = (1 / base) * to_power(base, power)
    
    elif power == 0:
        ans = 1
        
    else:
        ans = base
          
    return ans

def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    if len(s) > 1:
        c1 = s[0]
        c2 = s[-1]
        
        if not c1.isalpha():
            palindrome = is_palindrome(s[1:])
            
        elif not c2.isalpha():
            palindrome = is_palindrome(s[:-1])
            
        elif c1.lower() == c2.lower():
            palindrome = is_palindrome(s[1:-1])
            
        else:
            palindrome = False
            
    else:
        palindrome = True
        
    return palindrome

def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    if bag == []:
        new_set = []

    else:
        new_set = bag_to_set(bag[:-1])

        if bag[-1] not in new_set:
            new_set.append(bag[-1])

    return new_set  
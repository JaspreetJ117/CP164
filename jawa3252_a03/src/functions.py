"""
-------------------------------------------------------
Assgn | Functions.py | Array Based Stack | ADT
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-22"
-------------------------------------------------------
"""

from Stack_array import Stack

# constants 
OPERATORS = "+-*/"

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    i = 0
    target1 = Stack()
    target2 = Stack()
    
    while not source.is_empty():
        i += 1
        value = source.pop()
        
        if i%2 == 0:
            target1.push(value)
        
        else:
            target2.push(value)
            
    return target1, target2

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp_stack = Stack()

    while not source.is_empty():
        temp_stack.push(source.pop())

    while not temp_stack.is_empty():
        source.push(temp_stack.pop())
        
    return 

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    cleaned_string = ""
    
    palindrome = True

    for char in string:
        if char.isalnum():
            cleaned_string += char.lower()

    for char in cleaned_string[:len(cleaned_string) // 2]:
        stack.push(char)

    start_index = len(cleaned_string) // 2
    if len(cleaned_string) % 2 != 0:
        start_index += 1

    for char in cleaned_string[start_index:]:
        if stack.is_empty() or stack.pop() != char:
            palindrome = False

    return palindrome

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    
    stack = Stack()

    elements = string.split()

    for element in elements:
        if element in OPERATORS:
            right_operand = stack.pop()
            left_operand = stack.pop()

            if element == '+':
                stack.push(left_operand + right_operand)
            elif element == '-':
                stack.push(left_operand - right_operand)
            elif element == '*':
                stack.push(left_operand * right_operand)
            elif element == '/':
                stack.push(left_operand / right_operand)
        else:
            stack.push(float(element))

    answer = stack.pop()
    
    return answer

def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to an operating string
    and returns a new list of values. values_in is unchanged.
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    values_out = []
    railline = Stack()
    values_copy = values_in[:]  
    
    for char in opstring:
        if char == 'S':
            if values_copy:
                railline.push(values_copy.pop(0))
            else:
                values_out =  None  
        elif char == 'X':
            if not railline.is_empty():
                value = railline.pop()
                values_out.append(value)
            else:
                values_out = None  
        else:
            values_out = None  
    
    return values_out

        
        

    
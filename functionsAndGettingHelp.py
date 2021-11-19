# Question 1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num,2)

# Question 2
# The help for round says that ndigits (the second argument) may be negative. What do you think will happen when it is? Try some examples in the following cell.
num = 987.568
round(num,-1)
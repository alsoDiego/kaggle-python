# q1
def sign(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1
​
# q2a
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)


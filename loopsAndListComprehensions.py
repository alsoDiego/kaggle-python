# q1
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    cont = 0
        for num in nums:
            if num % 7 == 0:
                cont =+ 1
        if cont > 0:
            return True
        else:
            return False

"""
My solution passed all tests. The given solutions are:

    def has_lucky_number(nums):
        for num in nums:
            if num % 7 == 0:
                return True
        # We've exhausted the list without finding a lucky number
        return False

    def has_lucky_number(nums):
        return any([num % 7 == 0 for num in nums])
"""

# q2
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    is_greater = []
    for i in L:
        is_greater.append(i > thresh)
    
    return is_greater

"""
My solution passed all tests. The another given solution is:

    def elementwise_greater_than(L, thresh):
        return [ele > thresh for ele in L]
"""


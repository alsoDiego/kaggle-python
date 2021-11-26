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


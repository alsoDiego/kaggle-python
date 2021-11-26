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

# q3
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    i = 0
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

# q4
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    pass

    ### Given solution:
    """
    The exact expected value of one pull of the slot machine is 0.025 - i.e. a little more than 2 cents. See? Not every game in the Python Challenge Casino is rigged against the player!

    In order to get this answer, you'll need to implement the estimate_average_slot_payout(n_runs) function to simulate pulling the slot machine n_runs times. It should return the payout averaged over those n_runs.

    Then, once the function is defined, in order to estimate the average slot payout, we need only call the function.

    Because of the high variance of the outcome (there are some very rare high payout results that significantly affect the average) you might need to run your function with a very high value of n_runs to get a stable answer close to the true expectation. For instance, you might use a value for n_runs of 1000000.

    Here's an example for how the function could look:
    """
    def estimate_average_slot_payout(n_runs):
        # Play slot machine n_runs times, calculate payout of each
        payouts = [play_slot_machine()-1 for i in range(n_runs)]
        # Calculate the average value
        avg_payout = sum(payouts) / n_runs
        return avg_payout


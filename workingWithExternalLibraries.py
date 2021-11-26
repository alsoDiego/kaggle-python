# q1
# Given solution:
def prettify_graph(graph):
    graph.set_title("Results of 500 slot machine pulls")
    # Make the y-axis begin at 0
    graph.set_ylim(bottom=0)
    # Label the y-axis
    graph.set_ylabel("Balance")
    # Bonus: format the numbers on the y-axis as dollar amounts
    # An array of the values displayed on the y-axis (150, 175, 200, etc.)
    ticks = graph.get_yticks()
    # Format those values into strings beginning with dollar sign
    new_labels = ['${}'.format(int(amt)) for amt in ticks]
    # Set the new labels
    graph.set_yticklabels(new_labels)

# q2
# Given solution:
"""
Solution: Luigi used the variable name i to represent each item in racer['items']. However, he also used i as the loop variable for the outer loop (for i in range(len(racers))). These i's are clobbering each other. This becomes a problem only if we encounter a racer with a finish of 1 and a name of None. If that happens, when we try to print the "WARNING" message, i refers to a string like "green shell", which python can't add to an integer, hence a TypeError.

This is similar to the issue we saw when we imported * from math and numpy. They both contained variables called log, and the one we got when we tried to call it was the wrong one.

We can fix this by using different loop variables for the inner and outer loops. i wasn't a very good variable name for the inner loop anyways. for item in racer['items'] fixes the bug and is easier to read.

Variable shadowing bugs like this don't come up super often, but when they do they can take an infuriating amount of time to diagnose!
"""


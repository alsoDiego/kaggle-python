# q0
"""
Let's start with a string lightning round to warm up. What are the lengths of the strings below?

For each of the five strings below, predict what len() would return when passed that string. Use the variable length to record your answer, then run the cell to check whether you were right.
"""

# q0a
a = ""
length = 0

# q0b
b = "it's ok"
length = 7

# q0c
c = 'it\'s ok'
length = 7

# q0d
d = """hey"""
length = 3

# q0e
e = '\n'
length = 1

# q1
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return (len(zip_code) == 5) and zip_code.isdigit()


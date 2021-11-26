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

# q2
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    
    # list to hold the indices of matching documents
    matches = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            matches.append(i)
    return matches


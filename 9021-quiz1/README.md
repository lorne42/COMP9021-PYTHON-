# Written by *** for COMP9021
#
# Prompts the user for an integer at least equal to 3 and for the
# name of a file, assumed to be stored in the working directory.
#
# The file can contain anywhere any number of blank lines
# (that is, lines containing an arbitrary number of spaces
# and tabs--an empty line being the limiting case).
#
# Nonblank lines are always of the form:
#                Give me that_many characters
# with any number of spaces at the beginning and at the end of the line
# (possibly none) and with at least one space between successive words,
# where that_many is one of 2, 3, 4, 5, 6, 7, 8 or 9
# and where characters is one of dashes, stars, carets or dollars.
#
# Outputs text and "pictures" based on the provided input.
#
# Tip: Use a dictionary that maps 2 to the word two, 3 to the word three...
#      Use another dictionary that maps the word dashes to the character -,
#      the word stars to the character *...

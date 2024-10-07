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


import sys
from os.path import exists

try:
    size = int(input('Enter an integer at least equal to 3: '))
    if size < 3:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
file_name = input('Input the name of a file '
                 'in the working directory: '
                ).removesuffix('\n')
if not exists(file_name):
    print('Incorrect input, giving up.')
    sys.exit()



# INSERT YOUR CODE HERE

# table:
print('Here is your coffee table of size %d:'%size)
print(' '+'-'* size)
print('/|'+(size-2) *' '+'/|')
print('-'* size)
print('|'+(size-1)*' '+'|')

#give me sth:

 #dictionary
numD={'2':'two'  ,'3':'three','4':'four',
      '5':'five' ,'6':'six'  ,'7':'seven',
      '8':'eight','9':'nine' ,}

wD={'dollars':'$','stars':'*','carets':'^','dashes':'-'}

 #func
f = open(file_name , 'r')
lines=f.readlines()
for line in lines:
    if not line.isspace():
     d=line.split()
     print('Here are your '+numD[d[2]]+' '+d[3]+':')
     print(int(d[2])*wD[d[3]])
 

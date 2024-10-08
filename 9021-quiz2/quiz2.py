from random import seed, shuffle
import sys


try: 
    your_list = [int(x) for x in
                     input('Enter a permutation of 0, ..., n '
                           'for some n >= 0: '
                          ).split()
                ]
    if not your_list:
        raise ValueError
    your_list_as_set = set(your_list)
    if len(your_list_as_set) != len(your_list)\
       or your_list_as_set != set(range(len(your_list))):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try: 
    for_seed, length =\
        (int(x) for x in input('Enter two integers, '
                               'the second one between 0 and 10: '
                              ).split()
        )
    if not 0 <= length <= 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
my_list = list(range(length))
shuffle(my_list)
print('Here is your list:')
print('  ', your_list)
print('Here is my list:')
print('  ', my_list)

# INSERT THE FIRST PART OF YOUR CODE HERE
while len(your_list)!=0:
    f=0
    if your_list[0]==max(your_list) or your_list[0]==min(your_list):
        your_list.remove(your_list[0])
        f=1
    else: 
        if your_list[-1]==max(your_list) or your_list[-1]==min(your_list):
            your_list.remove(your_list[-1])
            f=1
    if f==0:
        break

print()
print('Removing again and again the currently largest\n'
      'or smallest element in your list for as long as\n'
      'it currently starts or ends the list, we get:'
     )
print(your_list)
print()
print("That's how to travel in my list:")

# INSERT THE SECOND PART OF YOUR CODE HERE
print(my_list.index(0)*'  '+'0')
for i in range(1,len(my_list)):
    if my_list.index(i)>my_list.index(i-1):
        print(my_list.index(i-1)*'  '+'--'*(my_list.index(i)-my_list.index(i-1))+'%d' %i)
    else:
         print(my_list.index(i)*'  '+'%d' %i+'--'*(my_list.index(i-1)-my_list.index(i)))

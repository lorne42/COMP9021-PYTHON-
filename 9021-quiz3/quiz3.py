
# Written by *** for COMP9021
#
# Implements a function that takes as argument a string
# consisting of arrows pointing North, East, South or West.
#
# Following the provided directions,
# - if the exploration gets back to the starting point, then this
#   common location will be represented by a black circle;
# - otherwise, the starting point will be represented by a blue circle
#   and the final destination by a red circle.

# All other visited locations will be represented by a square, of colour:
# - yellow if visited exactly once, 6 times, 11 times, 16 times...
# - orange if visited exactly twice, 7 times, 12 times, 17 times...
# - brown if visited exactly trice, 8 times, 13 times, 18 times...
# - green if visited exactly 4 times, 9 times, 14 times, 19 times...
# - purple if visited exactly 5 times, 10 times, 15 times, 20 times...

# The explored area is displayed within the smallest rectangle in
# which it fits; all unvisited locations within that rectangle are
# represented by white squares.
#
# The code points of the characters involved in this quiz are:
# 9899, 11036, 128308, 128309, 128999, 129000, 129001, 129002, 129003



def explore_this_way(directions):
    x=0 
    y=0
    max_x=0
    max_y=0
    min_x=0
    min_y=0
    dic_m={(0,0) : 1}
    if len(directions)==0:
        print('\u26AB')
    else:
        for i in directions:
            if i=='\u2b95':
                x+=1
                if max_x<x:
                    max_x=x
                if (x,y) in dic_m:
                    dic_m[(x,y)]+=1
                else:
                    dic_m[(x,y)]=1   
            elif i=='\u2b05':
                x-=1
                if min_x>x:
                    min_x=x
                if (x,y) in dic_m:
                    dic_m[(x,y)]+=1
                else:
                    dic_m[(x,y)]=1
            elif i=='\u2b06':
                y+=1
                if max_y<y:
                    max_y=y
                if (x,y) in dic_m:
                    dic_m[(x,y)]+=1
                else:
                    dic_m[(x,y)]=1
            elif i=='\u2b07':
                y-=1
                if min_y>y:
                    min_y=y
                if (x,y) in dic_m:
                    dic_m[(x,y)]+=1
                else:
                    dic_m[(x,y)]=1
        for a in range(max_y,min_y-1,-1):
            for b in range(min_x,max_x+1):
                if (a!=y or b!=x )and (a!=0 or b!=0):
                    if (b,a)not in dic_m.keys():
                        print('\u2b1c',end='')
                    elif dic_m[(b,a)]%5==1:
                        print('\U0001F7E8',end='')
                    elif dic_m[(b,a)]%5==2:
                        print('\U0001F7E7',end='')
                    elif dic_m[(b,a)]%5==3:
                        print('\U0001F7EB',end='')
                    elif dic_m[(b,a)]%5==4:
                        print('\U0001F7E9',end='')
                    elif dic_m[(b,a)]%5==0 and dic_m[(a,b)]!=0:
                        print('\U0001F7EA',end='') 
                elif a==y and b==x:
                    if x==0 and y==0:
                        print('\u26AB',end='')
                    else:
                        print('\U0001F534',end='')
                elif a==0 and b==0:
                    if x!=0 or y!=0:
                        print('\U0001F535',end='')
            print('\n',end='')
explore_this_way('\u2b06'*4+'\u2b07'*4+'\u2b95'*3)

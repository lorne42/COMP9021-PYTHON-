# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the function change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by *** and Eric Martin for COMP9021


from math import sqrt

class Point():
    def __init__(self, x = None, y = None):
        if x == None and y == None:
            self.x = 0
            self.y = 0
        elif x == None or y == None:
            print('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y

    # Write code for a function named collinear

class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
        if point_1.collinear(point_2, point_3):
            self.error_message('Initialisation')
        else:
            self._initialise(point_1, point_2, point_3)

    def error_message(self, phase):
        if phase == 'Initialisation':
            print('Incorrect input, triangle not created.')
        else:
            print('Incorrect input, triangle not motified.')

    def change_point_or_points(self, *, point_1 = None,
                                        point_2 = None,
                                        point_3 = None):
        pass
        # Replace pass above with your code

    def _initialise(self, p1, p2, p3):
        pass
        # Replace pass above with your code

    # Possibly define other functions

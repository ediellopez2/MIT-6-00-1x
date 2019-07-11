# Author: Ediel Lopez
# Date: July 9, 2019
# Course: MIT 6.00.1x - Midterm
#
#


def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    INPUT:
        - Assumes L is a list of integers
        - Assume functions f and g are defined for you.
            - f takes in an integer, applies a function, returns another integer
            - g takes in an integer, applies a Boolean function,
            returns either True or False
    FUNCTION:
        -  Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    RETURN:
        - Returns the largest element in the mutated L or -1 if the list is empty
    """
    if len(L) == 0:
        return -1
    else:
        new_list = []
        for index in L:
            if g(f(index)) == True:
                 new_list.append(index)

        L[:] = new_list

        if len(L) > 0:
             return max(L)


L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)

L = []
print(applyF_filterG(L, f, g))
print(L)
# Author: Ediel Lopez
# Date: July 9, 2019
# Course: MIT 6.00.1x - Midterm
#
# Write a recursive procedure, called laceStringsRecur(s1, s2),
# which also laces together two strings.


def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:],s2[1:],out+s1[0]+s2[0])
    return helpLaceStrings(s1, s2, '')

name_1 = "ediel"
name_2 = "nicholas"
print(laceStringsRecur(name_1,name_2))
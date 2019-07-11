# Author: Ediel Lopez
# Date: July 9, 2019
# Course: MIT 6.00.1x - Midterm
#
# Write a Python function that returns the sublist of strings in aList that contain
# fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"],
# your function should return: ["cat", "dog"]

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    myList = []
    for index in aList:
        if len(index) < 4:
            myList.append(index)

    return myList

print(lessThan4(["apple", "cat", "dog", "banana"]))
print(lessThan4(["ediel","nicholas","Jon"]))
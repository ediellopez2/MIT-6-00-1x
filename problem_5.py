# Author: Ediel Lopez
# Date: July 9, 2019
# Course: MIT 6.00.1x - Midterm
#
# Write a Python function that returns a list of
# keys in aDict with the value target

def keysWithValue(aDict, target):
    '''
    INPUT:
        aDict: a dictionary
        target: an integer
    RETURN:
        A list of keys sorted in increasing order.
    '''
    myList = []
    for key,value in aDict.items():
        if (value == target):
            myList.append(key)

    return sorted(myList)


print(keysWithValue({0: 2, 2: 3, 5: 2, 6: 0, 8: 1, 9: 1, 10: 0}, 2))
# Solution: [0,5]

print(keysWithValue({2: 3, 3: 1, 4: 1, 5: 3, 6: 1, 9: 1, 10: 1}, 3))
# Solution: [2,5]
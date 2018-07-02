# Author: Ediel Lopez
# Date: 7/1/2018
# Week 1 Problem 2
# Description: Print the number of times the string 'bob' occurs in s. 
#   For example, for the string s = 'azcbobobegghakl' the program will 
#   print: Number of times bob occurs is: 2


s = 'azcbobobegghakl'
left = 0            # Left edge of string
right = 3           # Right edge of string
maxRight = len(s) - 3       # Max Right edge of string
count = 0

while left <= maxRight:
    if s[left:right] == 'bob':
        count += 1
    left += 1
    right += 1
print("Number of times bob occurs is: " + str(count))
# Author: Ediel Lopez
# Date: 7/1/2018
# Week 1 Problem 1
# Description: This program calculates the number of times
#   that vowels appear in a given string s.

s = 'azcbobobegghakl'

count = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print("Number of vowels:",count)
# Author: Ediel Lopez
# Date: 7/1/2018
# Week 1 Problem 3
# Description: prints the longest 
#   substring of phrase in which the letters 
#   occur in alphabetical order. In the case 
#   of ties, print the first substring. 

#phrase = 'abcpghrjshrklmnopqyjfhjehyopqrstuvwxyz'
phrase = 'rtwuzksqbtkeqvddip'
defaultString = ''
longestString = ''
size = len(phrase) - 1

for index in range(size):
    # add the current char to defaultString if the current char is less 
    # than or equal to the next char 
    if phrase[index] < phrase[index+1] or phrase[index] == phrase[index+1]:
        defaultString += phrase[index]
    # In the event that the next char is not bigger revert backwards. Check to see 
    # if the current char is greater than the one that came before it. If so, add it
    # to defaultString
    elif phrase[index] >= phrase[index-1]:
        defaultString += phrase[index]
        if len(defaultString) > len(longestString): 
            longestString = defaultString   # If defaultString is longer than the longestString
            defaultString = ''              # make it the longsetStriing. 
        else:
            defaultString = ''              # Otherwise, clear defaultString
if len(defaultString) >= len(longestString):    # Do a final check, in case second-to-last character
    longestString = defaultString               # made defaultString longer than longestString

# If the second-to-last string is in longsetString check to see if the second-to-last char is smaller than
# the last char in phrase. If it is, add it to longestString. 
if phrase[size-1] in longestString and phrase[size-1] < phrase[size]:
    longestString += phrase[size]
    
    
print("Final String: " + longestString)
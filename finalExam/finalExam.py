
# ======================== Final Exam - Problem 3 =========================
# Write a function is_triangular that meets the specification below. A
# triangular number is a number obtained by the continued summation of
# integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc.,
# corresponding to 1, 3, 6, 10, etc., are triangular numbers.

##def is_triangular(n):
##    if n == 0:
##        return False
##    # The value n has to be an int and greater than 0.
##    if type(n) == int and n > 0:
##        sum = 0
##        for i in range(1,n+1):
##            sum = sum+i
##            # Return True if the sum is equal to n. 
##            if sum == n:
##                return True
##        return False
##    else:
##        return False
##
##
##print(is_triangular(1))
##print(is_triangular(2))
##print(is_triangular(3))
##print(is_triangular(4))
##print(is_triangular(5))
##print(is_triangular(6))
##print(is_triangular(91))



# ======================== Final Exam - Problem 4 =========================

##def longest_run(L):
##    """
##    Assumes L is a list of integers containing at least 2 elements.
##    Finds the longest run of numbers in L, where the longest run can
##    either be monotonically increasing or monotonically decreasing. 
##    In case of a tie for the longest run, choose the longest run 
##    that occurs first.
##    Does not modify the list.
##    Returns the sum of the longest run. 
##    """
##    increasing = []
##    previous_inc = []
##    
##    decreasing = []
##    previous_dec = []
##    
##    if isinstance(L, list) and len(L) > 1:
##        # =============== INCREASING ===================
##        if L == sorted(L):
##            increasing = L.copy()
##        else:
##            increasing.append(L[0])
##            for index in range(1,len(L)):  
##                if L[index] > L[index-1] or L[index] == L[index-1]:
##                    if L[index-1] < L[index] and L[index-1] not in increasing:
##                        increasing.append(L[index-1])
##                    increasing.append(L[index])
##                elif L[index] < L[index-1]:
##                    # print(increasing)
##                    if len(increasing) > len(previous_inc): 
##                        previous_inc = increasing[:]       
##                        increasing = []                  
##                    else:
##                        increasing = []
##            increasing, previous_inc = previous_inc[:],increasing[:]
##
##        
##        # ================== DECREASING ======================
##        if max(L) == L[0] and min(L) == L[-1]:
##            decreasing = L.copy()
##        else:
##            decreasing.append(L[0])
##            
##            for index in range(1,len(L)):  
##                if L[index] < L[index-1] or L[index] == L[index-1]:
##                    decreasing.append(L[index])
##                elif L[index] > L[index-1]:
##                    if len(decreasing) > len(previous_dec): 
##                        previous_dec = decreasing[:]       
##                        decreasing = []                  
##                    else:
##                        decreasing = []
##
##            decreasing, previous_dec = previous_dec[:],decreasing[:]
##    return max(sum(increasing),sum(decreasing))
##        
##
##
##L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
##print(longest_run(L))
##
##L = [5, 4, 10]
##print(longest_run(L))
##
##L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
##print(longest_run(L))
##
##L = [100000, 10000, 1000, 100, 10, 8, 8, 5, 2, 1, 0]
##print(longest_run(L))


# ======================== Final Exam - Problem 5 =========================
# Assume you are given two dictionaries d1 and d2, each with integer keys
# and integer values. You are also given a function f, that takes in two
# integers, performs an unknown operation on them, and returns a value.

# Write a function called dict_interdiff that takes in two dictionaries
# (d1 and d2). The function will return a tuple of two dictionaries: a
# dictionary of the intersect of d1 and d2 and a dictionary of the difference
# of d1 and d2

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
        # Ensure that both arguments are dictionaries
    assert type(d1) == dict and type(d2) == dict

    hit = {}
    miss = {}

    # I'm creating two dictionaries of key-value pairs that have a key-value pair in common (hit)
    # and not in common (miss).
    for key in sorted(d1.keys()):
        if key in d2.keys():
            hit[key] = d1[key] + d2[key]
        else:
            miss[key] = d1[key]

    for key in sorted(d2.keys()):
        if key not in hit.keys():
            miss[key] = d2[key]

    # I'm sorting the dictionary in increasing order based on the key.
    temp = {}
    for key in sorted(miss.keys()):
        temp[key] = miss[key]

    # print(hit)
    # print(miss)

    return (hit, temp)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1,d2))

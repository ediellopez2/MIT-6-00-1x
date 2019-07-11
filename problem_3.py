# Author: Ediel Lopez
# Date: July 9, 2019
# Course: MIT 6.00.1x - Midterm
#
# Write a recursive Python function, given a non-negative
# integer N, to count and return the number of occurrences of the digit 7 in N.
def count7(N):
    '''
    N: a non-negative integer
    '''
    hits = 0
    if (N <= 1):
        return 0
    else:
        num = N % 10    # Get the rightmost digit
        N = N // 10     # Remove the rightmost digit

        if num == 7:
            hits += 1

        return hits + count7(N)

    ##### Non-recursive Approach #####
    # hits = 0
    # while not(N <= 1):
    #     num = N % 10
    #     N = N // 10
    #     if num == 7:
    #         hits += 1
    # return hits

print(count7(1237123))
print(count7(717))
print(count7(8989))


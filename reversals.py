import math

def reverse_me(s, n):
    #Iterative algorithm that reverses a sequence of n elements.
    #Swaps first and last values, then second and second-to-last values,
    #until the middle of the sequence is reached.

    #Input: s - a sequence of any type; n - the number of values in the sequence
    #Output: None, the sequence is reversed in place
    for i in range(0,math.floor(n/2)):
        temp = s[i]
        s[i] = s[n-(i+1)]
        s[n-(i+1)] = temp
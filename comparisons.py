def middle_value(a,b,c):
    #Return the middle value of 3 numbers
    #Assumes that a,b,c are distinct
    largest = a
    second_largest = b

    #switch the values if b is larger than a
    if(b > a):
        largest = b
        second_largest = a

    #Now compare the values of largest and second_largest with c
    if(c > largest):
        #here c is the largest and the previous value of large must be second_largest
        second_largest = largest
    else:
        #here c is in between largest and second_largest, so c is the value of second_largest
        if(c > second_largest):
            second_largest = c
    return second_largest

def large1_large2(s,n):
    #Algorithm returns the largest and second_largest value in a sequence of n elements
    #input: s - an unsorted sequence of AT LEAST 2 values; n - the size of the sequence
    #output: largest & second_largest - the largest and second_largest value of the sequence
    largest = s[0]
    second_largest = s[1]

    #If s1 is greater, swap the values of largest and second_largest
    if(s[1] > s[0]):
        largest = s[1]
        second_largest = s[0]

    #Loop thru to the end of the sequence, comparing each value to large and second_largest
    for i in range(2,n):
        #Found a new large value-assign s[i] to largest, assign previous largest to second_largest
        if(s[i] > largest):
            temp = largest
            largest = s[i]
            second_largest = temp
        #s[i] is not largest, but could be second largest
        else:
            #If it is, assign s[i] to large
            if(s[i] > second_largest):
                second_largest = s[i]

    #Ran thru the entire sequence, return the two largest values
    return largest, second_largest

def last_large_index(s,n):
    #Algorithm returns the index of last occurence of the largest value in a sequence of n elements
    #input: s - sequence of unsorted values of AT LEAST 1 value; n - the size of the sequence
    #output: largest_index - the index of the last occurrence of the largest value
    largest = s[0]
    largest_index = 0

    for i in range(1,n):
        if(s[i] >= largest):
            largest = s[i]
            largest_index = i

    return largest_index
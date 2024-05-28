# start the pointer for both the arrays 
# start traversing both the array but seqeunce should be traverse first 
# if two value from both the array matches, increment in sequnce 
# if the values don't match then increment the array 
# if sequnce lenth is over return True 
# else return false 



def Solution1(array, sequence):

    arrayindexPointer = 0
    sequenceindexpointer = 0

    while arrayindexPointer < len(array) and sequenceindexpointer < len(sequence):
        if array[arrayindexPointer] == sequence[sequenceindexpointer]:
            sequenceindexpointer += 1
        arrayindexPointer += 1

    return print(sequenceindexpointer == len(sequence))

# not very sure about the condition where sequence didn't match

def Solution2(array, sequence):
    arrayindexPointer = 0
    sequenceindexpointer = 0 

    for i in array:
        for j in sequence:
            if sequenceindexpointer == len(sequence):
                break
            if i == j:
                sequenceindexpointer += 1
    return sequenceindexpointer == len(sequence)



array = [5,1,22,25,6,-1,8,10]
sequence =[1,6,-1,10]
Solution2(array, sequence)
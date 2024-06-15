
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest_dif = float("inf")
    current_dif = float("inf")
    pair = []
    while idxOne < len(arrayOne) and idxTwo(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        current_dif = abs(firstNum-secondNum)
        if firstNum > secondNum:
            idxOne += 1

        elif secondNum > firstNum:
            idxTwo += 1

        else:
            return [firstNum, secondNum]
        
        if current_dif > smallest_dif:
            smallest_dif = current_dif
            pair = [firstNum, secondNum]
    
    return pair




# arrayOne = [-1,5,10,20,28,3]
# arrayTwo = [26,134,135,15,17]
arrayOne = [-1, 5, 10, 20, 3]
arrayTwo =  [26, 134, 135, 15, 17]

smallestDifference(arrayOne, arrayTwo)
[1,2,4,5,26,7,9,0]

def Solution1(array):

    SortedArray = [ 0 for _ in array]

    for idx in range(len(array)):
         value = array[idx]
         SortedArray[idx] = value * value

    SortedArray.sort()

    return SortedArray

     


def Solution2(array):

    SortedArray =  [0 for _ in range(len(array))]

    smallerIdx = 0
    largerIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerIdxValue = array[smallerIdx]
        largerIdxValue = array[largerIdx]

        if abs(smallerIdxValue) > abs(largerIdxValue):
            SortedArray[idx] = smallerIdxValue * smallerIdxValue
            smallerIdx += 1
        else:
            SortedArray[idx] = largerIdxValue * largerIdxValue
            largerIdx -= 1

    return SortedArray




# problem
array = [-7,-5,-4,3,6,8,9]
Solution1(array)
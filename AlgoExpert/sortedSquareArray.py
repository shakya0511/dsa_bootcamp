[1,2,4,5,26,7,9,0]

def Solution1(array):

    SortedArray = [ 0 for _ in array]

    for idx in range(len(array)):
         value = array[idx]
         SortedArray[idx] = value * value

    SortedArray.sort()

    return SortedArray

    




def Solution2(array):

    zeroArray =  [0 for _ in range(len(array))]

    Idx1 = 0
    Idx2 = len(array) - 1
    ZeroIdx = len(zeroArray) - 1

    # Learning : deal with negative integers saperately 

    while Idx1 < len(array) -1 :
        sqr1 = (array[Idx1] * array[Idx1])
        sqr2 = (array[Idx2] * array[Idx2])

        if sqr1 < sqr2:
                zeroArray[ZeroIdx]= sqr2
                Idx2 -= 1
                ZeroIdx -= 1

        if sqr1 > sqr2:

            if array[Idx1] and array[Idx2] > 0:   
                zeroArray[ZeroIdx] = sqr1
                Idx1 += 1
                ZeroIdx -= 1            
            if array[Idx1] and array[Idx2] < 0:
                zeroArray[ZeroIdx]= sqr1
                Idx1 += 1
                ZeroIdx -= 1

    return zeroArray

    






# array = [1,2,3,5,6,8,9]
# array = [-2, -1]
array = [-7,-5,-4,3,6,8,9]

Solution1(array)
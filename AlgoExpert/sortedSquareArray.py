[1,2,4,5,26,7,9,0]

def Solution1(array):

    output = []
    sorted = []

    for i in array:
        sqr = i*i 
        output.append(sqr)




def Solution2(array):

    zeroArray =  [0 for _ in range(len(array))]

    SIdx = 0
    EIdx = len(array) - 1
  
    while SIdx < len(array) and EIdx > 0:
        Fnum = (array[SIdx] * array[SIdx])
        Lnum = (array[EIdx ] * array[EIdx ])
        if Fnum > Lnum:
            if array[SIdx] < array[EIdx]:
                zeroArray[EIdx] = array[SIdx] * array[SIdx]
                if array[SIdx] > array[EIdx]:
                    zeroArray[EIdx] = array[EIdx] * array[EIdx]
            SIdx = SIdx + 1
                  
             
        if Fnum < Lnum:
            if array[SIdx] < array[EIdx]:
                zeroArray[EIdx] = array[EIdx] * array[EIdx]
                if array[SIdx] > array[EIdx]:
                    zeroArray[EIdx] = array[SIdx] * array[SIdx]
            EIdx = EIdx - 1

        if Fnum == Lnum:
            SIdx += 1
            EIdx -= 1

    return []






# array = [1,2,3,5,6,8,9]
# array = [-2, -1]
array = [-7,-5,-4,3,6,8,9]

Solution2(array)
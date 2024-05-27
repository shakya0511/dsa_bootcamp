# take element of sequence one by one and look for them in array
# store the index for match case and compare it with next index value should be greater than before


def Solution1(array, sequence):

    startArrP = 0
    startSeqP = 0

    for i in sequence:
        for j in array:
            if sequence[startSeqP] == array[startArrP]:
                startSeqP += 1
            else:
                startSeqP += 1
        return True
    return False

    


                    
                



array = [5,1,22,25,6,-1,8,10]
sequence =[1,6,-1,10]
Solution1(array, sequence)
# start 2 pointer p1 and p2 access the values
# declare one variable name swap == False
# campare the values if p1 > p2 then switch index, increment p1 and p2 by 1
# if p1 < p2, no swap, increment p1 and p2 by 1
# for first interation do it for whole array, decrement it for each itration by 1
# if value of that variable is equals to zero then array is sorted 


def Solution1 (array):

    isSorted = False 
    counter = 0 
    while not isSorted: # in loops True and false are not governed with = or == it should be like variable or not variable 
                        # use not as a tool to create loops 
        for i in range(len(array)- 1 - counter):
            isSorted = True
            if array[i] >= array[i+1]: # use of > is only restricted to the assumption that no equal repeat itself
                                        # >= will be used for 
                swap(i,i+1,array)      # don't think why swap is defined saperately grow a habit to break problems into pieces (remember OOPS ?)
                isSorted = False
            # else: 
            #     isSorted=True    ## leanring over here is don't use else at all so that is sorted will always remain false  
                                    # use each condition very carefully ask yourself do you really need a else condition ?
        counter += 1
    return print(array)

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]

array = [9,8,4,6,2,4,0,1,4]
Solution1(array)
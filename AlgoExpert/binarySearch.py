# create 3 pointer : start, end , mid 
# mid is sum of start index end index modulo 2 
# calculate mid 
# if mid is smaller than look up value then make start pointer = 0 end pointer = (mid - 1)
# if mid is larger than look up value then make start pointer = (mid + 1) and end pointer len(array)
# calulate mid point compare it with lookup value 
# repeat step 4 
# repeat step 5 
# if index of small pointer is greater than large pointer than lookup value not found in array
# assumption over here is the given array is sorted


def Solution1(array, target):
    smaller_pointer = 0
    larger_pointer = len(array) - 1
    
    while smaller_pointer <= larger_pointer:
        midIDx = (smaller_pointer + larger_pointer) // 2
        if target < array[midIDx]:
            larger_pointer = (midIDx - 1)

        if target > array[midIDx]:
            smaller_pointer = (midIDx + 1)

        if target == array[midIDx]:
            return midIDx
    
    return -1


def Solution2 (array, target):
    
    return helperFunc (array, target, 0, len(array) -1)

def helperFunc (array, target, left, right):
        
        if left > right:
             return -1
        midIdx = (left + right) // 2
        if target == array[midIdx]:
             return midIdx 
        elif target < array[midIdx]:
             return helperFunc(array, target, left, midIdx - 1 )
        else:
             return helperFunc(array, target, midIdx + 1, right)
             
    

array = [0, 22, 23, 34, 54, 44, 90]
target = 44

Solution2(array, target)
print("run")
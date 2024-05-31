
# loop over complete list and find the two values
# O(N^2) time | O(N) space 

def Solution1(array, targetSum):
    for i in range(len(array) - 1):
        numOne = array[i] 
        for j in range(i+1, len(array)):
            numTwo = array[j]
            if numOne + numTwo == targetSum:
                print(numOne)
                print(numTwo)
                return [numOne, numTwo]
    return []

# use x + y = targetSum
# y = targetSum - x
# if y is not is hash table then store it
# if y is in hash table then end the loop and print the values
 
def Solution2(array, targetSum):
    nums = {}
    for i in array:
        nums[i] = True
    for x in array:
        y = targetSum - x
        if y != x:
            if y in nums:
                return [x,y]
    return []

# sort the array
# point a pointer at intial and final values 
# sum the intial and final is something compare it with target some 
# if sum is less than targetSum value increment initial pointer
# if sum is greater than targetSum value decrement final value 


def Solution3(array, targetSum):
    array.sort()
    init_val = 0
    end_val = len(array) - 1
    while init_val < end_val:
        currentSum = array[init_val] + array[end_val]
        if currentSum == targetSum:
            return [array[init_val], array[end_val]]
        elif( currentSum < targetSum):
            init_val += 1
        elif( currentSum > targetSum):
            end_val -= 1
    return ["Test"]
    
            
array = [3,5,-4,8,11,1,-1,6]
targetSum = 10

# Solution1(array, targetSum)
# Solution2(array, targetSum)
Solution3(array, targetSum)

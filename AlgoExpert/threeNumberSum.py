def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []

    for i in range(len(array)-2):
        leftpointer = i + 1
        rightpointer = len(array)-1
        currentSum = array[i] + array[leftpointer] + array[rightpointer]
        while leftpointer < rightpointer:
            if currentSum == targetSum:
                triplets.append([array[i], array[leftpointer], array[rightpointer]])
                leftpointer += 1
                rightpointer -= 1
            elif currentSum < targetSum:
                leftpointer += 1
            elif currentSum > targetSum:
                rightpointer -= 1
    return triplets


array = [12,3,1,2,-6,5,-8,6]
targetSum = 0
threeNumberSum(array,targetSum)



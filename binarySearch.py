arr = [1,2,3,4,5,6,7,8,9,10]
start = 0
end = len(arr) - 1
target = 2

print(f"len is {len(arr)}")

def binarySearch(arr, start, end, target):
    print(f"array is : {arr},start point is : {start},end point is : {end},target is : {target}")
    
    while start < end:
        midIndex = (start+end)//2
        if arr[midIndex] == target:
            return print(f'target value {target} found')
        elif arr[midIndex] > target:
            return binarySearch(arr, start, midIndex-1, target)
        else:
            return binarySearch(arr, midIndex+1, end, target)
    

binarySearch(arr, start, end, target)
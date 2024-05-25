class MergeSort:
    def __init__(self, array):
        print("init is called here")
        self.array = array     # [38, 27, 43, 87, 0, 82, 4]
    def sort(self):
        print("\n\n")
        print("! -- sort is called here -- !")
        print(f"Array is -> {self.array}")
        self.array = self._merge_sort(self.array)

        return self.array
    
    def _merge_sort(self, arr):
        print("\n\n")
        print("! _merge_sort called here !")
        if len(arr) <= 1:
            print(f"global array is {self.array}")
            print(f"lenght of array is {len(arr)}")
            print(f"local array is {arr}")
            
            return arr
        

        print(f"! ....determining lenght of array.... !")
        mid = len(arr) // 2
        print(f"! mid is {mid} here !")
        left_half = arr[:mid]
        print(f"! left half is {left_half} here <-- !")
        right_half = arr[mid:]
        print(f"! right half {right_half} here --> !")

        left_half = self._merge_sort(left_half)
        right_half = self._merge_sort(right_half)
        print(f"! the global array is {self.array} !""\n")
        print(f"! the local array is {arr} !""\n")
        print(f'! this is Left Half{left_half} !'"\n")
        print(f'! this is right Half{right_half} !'"\n")

        print("! _merge_sort means breaking exits here !")

        return self._merge(left_half, right_half)
    
    def _merge(self, left, right):
        print("\n\n")
        print("! _merge is called here !")
        merged = []
        print(f"! this is merged array : {merged} !")
        left_index, right_index = 0, 0
        print(f"! left index is {left_index}, right index is {right_index} !")
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                print(f"! left value {left[left_index]} is less than right value {right[right_index]} !")
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                print(f"! right value {right[right_index]} is less than left value {left[left_index]} !")
                right_index += 1
        
        while left_index < len(left):
            merged.append(left[left_index])
            print(f"appending {left[left_index]} to merged")
            print(f"! single loop merged append, {merged} left <-- !")
            left_index += 1
        
        while right_index < len(right):
            merged.append(right[right_index])
            print(f"appending {right[right_index]} to merged")
            print(f"! single loop merged append, {merged} right--> !")
            right_index += 1

        print(" ! _merge means joining exits here !")

        return merged

# Example usage:
arr = [38, 27, 43, 87, 0, 82, 4]
merge_sorter = MergeSort(arr)
sorted_arr = merge_sorter.sort()
print("Sorted array:", sorted_arr)

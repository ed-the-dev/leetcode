from typing import List

def insertionSort(nums: List[int]) -> List[int]:

    for i in range(1, len(nums)):

        j_index = i - 1 

        while j_index >= 0 and nums[j_index] > nums[j_index+1]:

            nums[j_index], nums[j_index+1] = nums[j_index+1], nums[j_index]
            j_index -= 1

    return nums

def sortArray(nums: List[int]) -> List[int]:

    # Merge in-place
    def merge(arr, start, middle, end):
        # Copy the sorted left & right halfs to temp arrays
        L = arr[start: middle + 1]
        R = arr[middle + 1: end + 1]

        i = 0 # index for L
        j = 0 # index for R
        k = start # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
    def merge_sort(arr: list[int], start: int, end: int):

        if end - start  <= 0:
            return nums
        
        # The middle index of the array
        middle: int = (start + end) // 2

        # Sort the left half
        merge_sort(arr, start, middle)

        # Sort the right half
        merge_sort(arr, middle + 1, end)

        # Merge sorted halfs
        merge(arr, start, middle, end)
        
        return arr
    
    return merge_sort(nums, 0, len(nums))

print(sortArray([5,2,3,1]))
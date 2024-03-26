from typing import List

def removeElement(nums: List[int], val: int) -> int:

    index: int = 0

    while index < len(nums):

        if nums[index] == val:
            nums.pop(index)
        else:
            index+=1
        
        
    return len(nums)

        
print(removeElement([3,2,2,3], 3))
from typing import List

def removeDuplicates(nums: List[int]) -> int:

    counter = 0
    current: int = None


    for numero in nums:

        if numero == current:
            continue

        else:
            current = numero
            nums[counter] = numero
            counter += 1

    return counter


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
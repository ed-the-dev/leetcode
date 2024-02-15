from typing import List

def containsDuplicate(nums: List[int]) -> bool:

    int_set: set = set()

    for num in nums:
        if num in int_set:
            return True
        else:
            int_set.add(num)
    return False

# Or could just convert the List into a Set, then compare lengths...



print(containsDuplicate([1,2,3,1]))
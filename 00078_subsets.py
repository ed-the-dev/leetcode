from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets: list[list[int]] = []

        current_set: list[int] = []

        def helper(index: int, current_set: list[int]):

            if index >= len(nums):
                subsets.append(current_set.copy())
                return

            current_set.append(nums[index])
            helper(index+1, current_set)

            current_set.pop()
            helper(index+1, current_set)
        
        helper(0, current_set)

        return subsets
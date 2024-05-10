from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        subsets: list[list[int]] = []

        current_set: list[int] = []

        def helper(index: int, current_set: list[int]):

            if index >= len(nums):
                subsets.append(current_set.copy())
                return
            
            # Choice to include the next number
            
            current_set.append(nums[index])
            helper(index+1, current_set)

            # Choice to not include the number and any of which are the same

            current_set.pop()

            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1

            helper(index+1, current_set)
        
        helper(0, current_set)

        return subsets
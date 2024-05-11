from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        permutations: list[list[int]] = []

        current_perm: list[int] = []

        counts: dict[int, int] = {number:0 for number in nums}

        for number in nums:
            counts[number] += 1

        def dfs_back_track():

            if len(current_perm) == len(nums):
                permutations.append(current_perm.copy())
                return
            
            for number in counts:

                if counts[number] > 0:

                    current_perm.append(number)
                    counts[number] -= 1
                    dfs_back_track()
                    current_perm.pop()
                    counts[number] += 1
        
        dfs_back_track()

        return permutations

            

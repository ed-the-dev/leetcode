from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations: list[list[int]] = [[]]

        for number in nums:
            next_permutations: list[list[int]] = []

            for permutation in permutations:
                for index in range(len(permutation)+1):
                    permutation_copy: list[int] = permutation.copy()
                    permutation_copy.insert(index, number)
                    next_permutations.append(permutation_copy)
                
            permutations = next_permutations
        
        return permutations
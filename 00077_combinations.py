from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations: list[list[int]] = []

        def helper(index: int, current_combination: list[int]):

            if len(current_combination) == k:
                combinations.append(current_combination.copy())
            
            if index > n:
                return 
            
            for j in range(index, n+1):
                current_combination.append(j)

                helper(j+1, current_combination)

                current_combination.pop()

        helper(1, [])

        return combinations
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combinations: list[list[int]] = []

        def helper(index: int, current_combination: list[int], total: int):

            if total == target:
                combinations.append(current_combination.copy())
                return

            if total > target or index == len(candidates):
                return
            
            # Choice where we pick the same number

            current_combination.append(candidates[index])
            helper(index, current_combination, total+candidates[index])

            # Choice where we move onto the next number

            current_combination.pop()
            helper(index+1, current_combination, total)
        
        helper(0, [], 0)

        return combinations



solution: Solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))
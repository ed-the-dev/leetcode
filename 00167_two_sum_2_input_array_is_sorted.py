from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left_pntr: int = 0
        right_pntr: int = len(numbers)-1

        while left_pntr != right_pntr:
            
            total:int = numbers[left_pntr] + numbers[right_pntr]
            if total == target:
                return [left_pntr+1, right_pntr+1]
            
            elif total > target:
                right_pntr -= 1

            else:
                left_pntr += 1

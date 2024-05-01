from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_length: int | float = float('inf')

        left: int = 0

        current_total: int = 0

        for right in range(len(nums)):
            current_total += nums[right]

            if current_total >= target:
                while current_total >= target:
                    min_length = min(right - left + 1, min_length)

                    current_total -= nums[left]
                    left += 1

        
        return min_length if min_length != float('inf') else 0
    

solution: Solution = Solution()
print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))

            
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum: int = nums[0]
        current_sum: int = 0

        for num in nums:

            current_sum += num

            max_sum = max(max_sum, current_sum)

            if current_sum < 1:
                current_sum = 0

        return max_sum
            

solution: Solution = Solution()

print(solution.maxSubArray([-3,-2,-3]))
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_sum: int = nums[0]
        current_max: int = 0

        min_sum: int = nums[0]
        current_min: int = 0

        total: int = 0

        for num in nums:
            current_max = max(0, current_max)
            current_max += num

            max_sum = max(max_sum, current_max)

            current_min = min(0, current_min)
            current_min += num

            min_sum = min(min_sum, current_min)

            total += num

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)



solution: Solution = Solution()
print(solution.maxSubarraySumCircular([1,-2,3,-2]))



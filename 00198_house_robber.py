from typing import List

class Solution:

    # I've written this back to front which makes it more confusing, but really no need to do that. 

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp: list[int] = [(nums[-3]+nums[-1]), nums[-2], nums[-1]]

        if len(nums) == 3:
            return max(dp[0], dp[1])

        for index in range(-4, -(len(nums)+1), -1):
            holder: int = max(nums[index]+dp[1], nums[index]+dp[2])

            dp[2] = dp[1]
            dp[1] = dp[0]
            dp[0] = holder

        return max(dp[0], dp[1])

solution: Solution = Solution()
print(solution.rob([1,2,3,1]))
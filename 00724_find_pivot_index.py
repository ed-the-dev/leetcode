from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum: list[int] = []

        for num in nums:
            prev: int = prefix_sum[-1] if len(prefix_sum) > 0 else 0
            prefix_sum.append(num + prev)

        for index in range(0, len(prefix_sum)):

            lhs = prefix_sum[index-1] if index > 0 else 0
            rhs = prefix_sum[len(prefix_sum)-1] - prefix_sum[index]

            if lhs == rhs:
                return index
        
        return -1

solution: Solution = Solution()

solution.pivotIndex([1,7,3,6,5,6])
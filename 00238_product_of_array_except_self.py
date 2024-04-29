from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result: list[int] = [0] * len(nums)

        for index in range(len(nums)-1, -1, -1):
            result[index] = nums[index] * (result[index+1] if index+1 < len(nums) else 1)

        for index in range(0, len(nums)):
            nums[index] = nums[index] * (nums[index-1] if index > 0 else 1)

        for index in range(0, len(nums)):
            result[index] = (result[index+1] if index+1 < len(nums) else 1) * (nums[index-1] if index > 0 else 1)
        
        return result
    
    def neetCodeSolution(self, nums: List[int]) -> List[int]:
        result: list[int] = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


        
solution: Solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.neetCodeSolution([1,2,3,4]))


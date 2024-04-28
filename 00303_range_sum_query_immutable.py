from typing import List

class NumArray:

    def __init__(self, nums: List[int]):

        self.prefix_sum: list[int] = []

        for num in nums:
            prev: int = self.prefix_sum[-1] if len(self.prefix_sum) > 0 else 0
            self.prefix_sum.append(num + prev)
        

    def sumRange(self, left: int, right: int) -> int:

        return self.prefix_sum[right] - (self.prefix_sum[left-1] if left > 0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

num_array: NumArray = NumArray([1,2,3])

print(num_array.prefix_sum)

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow: int = 0
        fast: int = 0

        meeting: int = None

        while True:
              slow = nums[slow]
              fast = nums[nums[fast]]

              if slow == fast:
                    meeting = slow
                    break
              
        slow_2: int = 0

        while True:
              slow_2 = nums[slow_2]
              meeting = nums[meeting]

              if slow_2 == meeting:
                    return slow_2
        
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set: set[int] = set(nums)

        longest: int = 0

        for num in nums:

            if num not in nums_set:
                continue
            
            starting_number: int = num
            longest_from_number: int = 1
            

            while num-1 in nums_set:
                longest_from_number += 1
                num -= 1
                nums_set.remove(num)
            
            num = starting_number
            while num + 1 in nums_set:
                longest_from_number += 1
                num += 1
                nums_set.remove(num)
            
            longest = max(longest, longest_from_number)

            # Run time is slightly better when I don't use this... :/
            nums_set.remove(starting_number)
        
        return longest
    

solution: Solution = Solution()
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

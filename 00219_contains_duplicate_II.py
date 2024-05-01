from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Window size is effectively k+1

        nums_positions: dict[int, list[int]] = {}

        for index in range(len(nums)):

            num: int = nums[index]

            if num in nums_positions:

                closest_index: int = nums_positions[num][-1]

                if index - closest_index <= k:
                    return True
                
                nums_positions[num].append(index)

            else:
                nums_positions[num] = [index]

        return False
    
solution: Solution = Solution()
print(solution.containsNearbyDuplicate([1,0,1,1], 1))

# Could have used a sliding window and a hashset which I add and remove from.
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def get_water(left_pntr: int, right_pntr: int) -> int:

            min_height: int = min(height[left_pntr], height[right_pntr])
            length: int = right_pntr - left_pntr

            return min_height * length
        
        l_pntr: int = 0
        r_pntr: int = len(height)-1

        global_max: int = 0

        while l_pntr != r_pntr:

            current_max: int = get_water(l_pntr, r_pntr)

            global_max = max(global_max, current_max)

            if height[l_pntr] > height[r_pntr]:
                r_pntr -= 1
            else:
                l_pntr += 1

        return global_max


        


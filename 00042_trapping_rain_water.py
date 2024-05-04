from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        total: int = 0

        prefix_heights = []

        for h in height:
            prefix_heights.append(h + prefix_heights[-1] if len(prefix_heights) > 0 else h)

        
        left_pntr: int = 0
        in_trough: bool = False

        for right_pntr in range(len(height)):

            if in_trough:
                if height[right_pntr] >= height[left_pntr]:

                    # import pdb
                    # pdb.set_trace()
                    # Then we have come to the end of a trough

                    min_height: int = min(height[left_pntr], height[right_pntr])

                    volume: int = min_height * (right_pntr-left_pntr-1)

                    no_of_blocks: int = prefix_heights[right_pntr-1]-prefix_heights[left_pntr]

                    water = volume - no_of_blocks

                    total += water

                    in_trough = False
                    left_pntr = right_pntr

                # right_pntr += 1
            
            if not in_trough:
                if right_pntr+1 < len(height) and  height[right_pntr + 1] < height[right_pntr]:
                    in_trough = True
                    left_pntr = right_pntr
                    # right_pntr += 1

        
        # Now get last section.

        last_heights: list[int] = height[left_pntr:]

        last_heights.reverse()

        prefix_heights = []

        for h in last_heights:
            prefix_heights.append(h + prefix_heights[-1] if len(prefix_heights) > 0 else h)

        
        left_pntr: int = 0
        in_trough: bool = False

        for right_pntr in range(len(last_heights)):

            if in_trough:
                if last_heights[right_pntr] >= last_heights[left_pntr]:

                    # import pdb
                    # pdb.set_trace()
                    # Then we have come to the end of a trough

                    min_height: int = min(last_heights[left_pntr], last_heights[right_pntr])

                    volume: int = min_height * (right_pntr-left_pntr-1)

                    no_of_blocks: int = prefix_heights[right_pntr-1]-prefix_heights[left_pntr]

                    water = volume - no_of_blocks

                    total += water

                    in_trough = False
                    left_pntr = right_pntr

                # right_pntr += 1
            
            if not in_trough:
                if right_pntr+1 < len(last_heights) and  last_heights[right_pntr + 1] < last_heights[right_pntr]:
                    in_trough = True
                    left_pntr = right_pntr



        return total






solution: Solution = Solution()

print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
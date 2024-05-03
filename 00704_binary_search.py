from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binary_search(left_pntr: int, right_pntr: int) -> int:

            # print("Left Pointer: %s" % left_pntr)
            # print("Right Pointer: %s" % right_pntr)
            
            # Find median value

            # Base cases

            if right_pntr - left_pntr  == 1:
                if nums[left_pntr] == target:
                    return left_pntr
                elif nums[right_pntr] == target:
                    return right_pntr
                else:
                    return -1
            
            if right_pntr - left_pntr == 0:
                if nums[left_pntr] == target:
                    return left_pntr
                else:
                    return -1
                

            median: int = (right_pntr + left_pntr) // 2

            # import pdb
            # pdb.set_trace()

            if nums[median] == target:
                return median
            
            elif nums[median] > target:
                return binary_search(left_pntr, median-1)
            
            else:
                return binary_search(median+1, right_pntr)
            
        return binary_search(0, len(nums)-1)
    

solution: Solution = Solution()

print(solution.search([-1,0,3,5,9,12], 9))

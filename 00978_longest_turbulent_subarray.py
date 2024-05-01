from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        max_turbulence: int = 0
        current_turbulence: int = 0

        next_sign_greater: bool = True

        for index in range(len(arr)):
            num: int = arr[index]

            if index == 0:
                current_turbulence += 1
                max_turbulence = max(max_turbulence, current_turbulence)
                continue
            
            if arr[index-1] is num:
                current_turbulence = 1
                max_turbulence = max(max_turbulence, current_turbulence)
                continue

            if current_turbulence == 1:
                current_turbulence += 1
                max_turbulence = max(max_turbulence, current_turbulence)

                if arr[index-1] > num:
                    next_sign_greater = False
                else:
                    next_sign_greater = True
                
                continue

            if arr[index-1] > num and next_sign_greater:
                current_turbulence += 1
                max_turbulence = max(max_turbulence, current_turbulence)
                next_sign_greater = False
            elif arr[index-1] < num and not next_sign_greater:
                current_turbulence += 1
                max_turbulence = max(max_turbulence, current_turbulence)
                next_sign_greater = True
            else:
                current_turbulence = 2
                max_turbulence = max(max_turbulence, current_turbulence)

                if arr[index-1] > num:
                    next_sign_greater = False
                else:
                    next_sign_greater = True
                    

        return max_turbulence

                
solution: Solution = Solution()
print(solution.maxTurbulenceSize([2,0,2,4,2,5,0,1,2,3]))

            

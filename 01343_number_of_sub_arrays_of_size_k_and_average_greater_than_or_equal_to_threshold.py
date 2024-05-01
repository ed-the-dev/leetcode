from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        count: int = 0

        def checkThreshold(total: int) -> int:
            if (total / k) >= threshold:
                 return 1
            return 0

        total = sum(arr[:k])

        count += checkThreshold(total)

        for left_pntr in range(1, len(arr)-k+1):
                right_pntr: int = left_pntr + k-1


                total -= arr[left_pntr-1]
                total += arr[right_pntr]

                count += checkThreshold(total)
        
        return count


solution: Solution = Solution()
print(solution.numOfSubarrays([11,13,17,23,29,31,7,5,2,3],3,5))
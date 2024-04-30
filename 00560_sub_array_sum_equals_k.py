from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixes: list[int] = []

        prefixes_counts: dict = {0: 1}

        count: int = 0

        for num in nums:

            prefix: int = num + (prefixes[-1] if prefixes else 0)
            
            difference: int = prefix - k

            if difference in prefixes_counts:
                count += prefixes_counts[difference]

            if prefix in prefixes_counts:
                prefixes_counts[prefix] += 1
            else:
                prefixes_counts[prefix] = 1
            
            prefixes.append(prefix)
             

        return count
    
solution: Solution = Solution()
print(solution.subarraySum([1,1,1], 2))

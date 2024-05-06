from typing import List
from math import ceil

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l: int = max(sum(piles) // h, 1)
        r: int = max(piles)

        best_rate: int = r

        while l <= r:

            # Also represents the rate we are testing
            middle: int = (l + r) // 2

            hours: int = 0
            for p in piles:
                hours += ceil(p/middle)
            
            if hours <= h:
                best_rate = min(best_rate, middle)
                r = middle - 1
            else:
                l = middle + 1

        return best_rate

    

    def minEatingSpeed_ineffecient_solution(self, piles: List[int], h: int) -> int:
        
        min_rate: int = max(sum(piles) // h, 1)

        max_rate: int = max(piles)

        current_minimum_rate: int = max_rate

        def check_rate_possible(rate: int) -> bool:

            if rate == 0:
                return False
            
            count = 0

            for index in range(0, len(piles)):
                
                count += ceil(piles[index]/rate)

            if count <= h:
                return True
            return False


        def search_space(lower_bound: int, upper_bound) -> int:

            middle: int = (lower_bound + upper_bound) // 2

            if check_rate_possible(middle):

                if not check_rate_possible(middle-1):
                    return middle
                
                else:

                    return search_space(lower_bound, middle-1)
            
            else:
                return search_space(middle + 1, upper_bound)
            
        return search_space(min_rate, max_rate)


    

solution: Solution = Solution()

print(solution.minEatingSpeed([312884470], 968709470))
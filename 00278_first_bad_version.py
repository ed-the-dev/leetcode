# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:

    raise NotImplementedError("This function is hidden, and part of the Leetcode Question.")

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def take_guess(lower: int, upper: int) -> int:

            middle: int = (lower + upper) // 2

            
            if isBadVersion(middle):
                if middle == 1:
                    return middle
                
                elif not isBadVersion(middle-1):
                    return middle
                else:
                    return take_guess(lower, middle-1)
                
            else:
                return take_guess(middle+1, upper)

        return take_guess(1, n) 


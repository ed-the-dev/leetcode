import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Clean up string

        string: str = re.sub(r"[^A-Za-z0-9]", "", s)

        string = string.lower()

        right_pntr: int
        left_pntr: int

        if len(string) % 2 == 0:
            right_pntr = len(string)//2
            left_pntr = right_pntr - 1

        else:
            left_pntr = right_pntr = len(string) // 2

        while right_pntr < len(string):
            if string[right_pntr] == string[left_pntr]:
                left_pntr -= 1
                right_pntr += 1
            else:
                return False
            
        return True


solution: Solution = Solution()

print(solution.isPalindrome("0P"))


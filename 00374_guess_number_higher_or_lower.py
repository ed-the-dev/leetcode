# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        def have_a_guess(lower: int, upper: int):
            middle: int = (upper + lower) // 2
            result: int = guess(middle)

            if result == 0:
                return middle
            elif result == -1:
                # guess is higher so try again
                return have_a_guess(lower, middle-1)
            else:
                return have_a_guess(middle+1, upper)

        return have_a_guess(0,n) 
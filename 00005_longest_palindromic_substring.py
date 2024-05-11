class Solution:
    def longestPalindrome(self, s: str) -> str:

        input: str = s

        longest_length: int = 0
        result: str = ''
        
        # Odd numbered case

        for index in range(len(input)):

            # print("\nIn odd numbered case")
            # print(index)

            current_length: int = 1

            left: int = index
            right: int = index

            while left >= 0 and right < len(input) and input[left] == input[right]:
                if (right - left + 1) > longest_length:
                    longest_length = right - left + 1
                    result = input[left: right+1]
                left -= 1
                right += 1


        # Even numbered case

        for index in range(len(input)-1):

            left: int = index
            right: int = index + 1

            current_length: int = 0

            while left >= 0 and right< len(input) and input[left] == input[right]:
                if (right - left + 1 ) > longest_length:
                    longest_length = right - left + 1
                    result = input[left: right + 1]
                left -= 1
                right += 1

        print(longest_length)
        return result

solution: Solution = Solution()

print(solution.longestPalindrome('babad'))

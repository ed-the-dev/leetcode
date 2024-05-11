class Solution:
    def countSubstrings(self, s: str) -> int:

        count: int = 0

        input: str = s

        # Odd case

        for index in range(len(input)):

            left: int = index
            right: int = index

            while left >= 0 and right < len(input) and input[left] == input[right]:
                count +=1
                left -= 1
                right += 1

        
        # Even case

        for index in range(len(input)-1):

            left: int = index
            right: int = index+1

            while left >= 0 and right < len(input) and input[left] == input[right]:
                count += 1
                left -= 1
                right += 1
        
        return count
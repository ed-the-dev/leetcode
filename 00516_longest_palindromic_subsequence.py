class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        input: str = s

        reversed: str = input[::-1]

        n_length: int = len(input)
        m_length: int = len(reversed)

        dp: list[int] = [0 for _ in range(m_length+1)]

        for row_index in range(n_length):

            current_row: list[int] = [0 for _ in range(m_length+1)]

            for column_index in range(m_length):

                if input[row_index] == reversed[column_index]:
                    current_row[column_index+1] = 1 + dp[column_index]
                
                else:
                    current_row[column_index+1] = max(current_row[column_index], dp[column_index+1])
            
            dp = current_row
        
        return dp[m_length]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n_length: int = len(text1)
        m_length: int = len(text2)

        dp: list[int] = [0 for _ in range(m_length+1)]

        for row_index in range(n_length):

            current_row: list[int] = [0 for _ in range(m_length+1)]

            for column_index in range(m_length):

                if text1[row_index] == text2[column_index]:
                    current_row[column_index+1] = 1 + dp[column_index]
                else:
                    current_row[column_index+1] = max(current_row[column_index], dp[column_index+1])
            
            dp = current_row
        
        return dp[m_length]
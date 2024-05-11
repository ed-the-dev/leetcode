class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp: list[int] = [1 for _ in range(n)]

        for _ in range(m-1):

            new_dp: list[int] = [0 for _ in range(n+1)]
            
            for index in range(n-1, -1, -1):

                new_dp[index] = new_dp[index+1] + dp[index]
            
            dp = new_dp

        return dp[0]

solution: Solution = Solution()
print(solution.uniquePaths(3, 7))
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        no_rows: int = len(obstacleGrid)

        no_cols: int = len(obstacleGrid[0])

        dp: list[int] = [0 for _ in range(no_cols+1)]
        dp[no_cols-1] = 1

        for row in range(no_rows-1, -1, -1):

            new_dp: list[int] = [0 for _ in range(no_cols+1)]

            for column in range(no_cols-1, -1, -1):

                if obstacleGrid[row][column] == 1:
                    new_dp[column] = 0
                else:
                    new_dp[column] = new_dp[column+1] + dp[column]

            dp = new_dp
        
        return dp[0]
    

solution: Solution = Solution()

print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))






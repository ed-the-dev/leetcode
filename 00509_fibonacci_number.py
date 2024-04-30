class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        dp: list[int] = [0, 1]

        for _ in range(2, n+1):
            next_fibonacci_number: int = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = next_fibonacci_number
        
        return dp[1]
    
solution: Solution = Solution()

print(solution.fib(3))


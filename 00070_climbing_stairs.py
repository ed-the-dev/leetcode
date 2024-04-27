class Solution:
    def climbStairs(self, steps: int) -> int:
        
        cache: dict = {} 

        def climb_stairs(current_step: int) -> int:

            if current_step in cache:
                return cache[current_step]
            
            if current_step == steps:
                return 1
            
            if current_step > steps:
                return 0
            
            value = 0

            value += climb_stairs(current_step + 1)

            value += climb_stairs(current_step + 2)

            cache[current_step] = value
            return value
        
        return climb_stairs(0)
    
    def bottom_up_dynamic_programming_climb_stairs(self, n: int) -> int:
        

        penultimate_step, one_before_penultimate = 1, 2
        
        if n == 1: return penultimate_step
        if n == 2: return one_before_penultimate
        
        for i in range(n-2):
            one_before_penultimate, penultimate_step  = penultimate_step + one_before_penultimate, one_before_penultimate
        
        return one_before_penultimate
            
    
solution: Solution = Solution()

print(solution.climbStairs(5))

print(solution.bottom_up_dynamic_programming_climb_stairs(5))
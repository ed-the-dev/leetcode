from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_counts: dict = {}

        counts_nums: dict[int, set] = {}

        for num in nums:
            
            # If number has already been seen, remove from current_counts...
            if num in nums_counts:
                current_count: int = nums_counts[num]

                counts_nums[current_count].remove(num)
                
                new_count = current_count + 1
                nums_counts[num] = new_count

                if new_count in counts_nums:
                    counts_nums[new_count].add(num)
                else:
                    counts_nums[new_count] = {num}
            
            else:

                nums_counts[num] = 1

                if 1 in counts_nums:
                    counts_nums[1].add(num)
                else:
                    counts_nums[1] = {num}

        result: list[int] = []

        for index in range(len(nums), -1, -1):

            if index in counts_nums:
                for value in counts_nums[index]:
                    if len(result) == k:
                        return result
                    result.append(value)
        
        return result
                    
                
solution: Solution = Solution()

# I could instead just iterate through getting key, and count,
# then bucket sort that dictionary. (Which is basically what I've done but no need to maintain two dicts as in my solution.)

print(solution.topKFrequent([1,1,1,2,2,3], 2))
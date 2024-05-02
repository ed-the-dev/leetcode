class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts: dict = {}
        result: int = 0

        left_pntr: int = 0
        for right_pntr in range(len(s)):

            counts[s[right_pntr]] = 1 + counts.get(s[right_pntr], 0)

            while (right_pntr - left_pntr + 1) - max(counts.values()) > k:
                counts[s[left_pntr]] -= 1
                left_pntr += 1

            result = max(result, (right_pntr - left_pntr + 1))

        return result





        
solution: Solution = Solution()
print(solution.characterReplacement("AABABBA", 1))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        global_max: int = 0

        left_pntr: int = 0

        characters: set = set()

        for character in s:
            
            while character in characters:
                characters.remove(s[left_pntr])
                left_pntr+=1

            characters.add(character)

            global_max = max(global_max, len(characters))

        return global_max

solution: Solution = Solution()
print(solution.lengthOfLongestSubstring('abcabcbb'))


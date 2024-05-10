from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        mapping: dict[int, list[str]] = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        combinations: list[str] = []

        def helper(index: int, current: str):

            if index == len(digits):
                combinations.append(current)
                return
            
            current_no: str = digits[index]
            
            for character in mapping[current_no]:
                current += character
                helper(index+1, current)
                current = current[:-1]

        helper(0,'')

        return combinations
        

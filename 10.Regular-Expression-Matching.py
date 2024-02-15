from typing import List

def isMatch(s: str, p: str) -> bool:

    # First read in p as a List of strings

    regex: List[str] = []

    for index, character in enumerate(p):
        if character != '*':
            next_index: int = index + 1

            if (next_index < len(p)):
                if p[next_index] == '*':
                    regex.append(p[index: next_index+1])
                else:
                    regex.append(p[index: next_index])
            else:
                regex.append(character)

    pntr1: int = 0

    options: List[List[tuple]] = []

    for expression in regex:

        expression_options: List[tuple] = []

        if len(expression) == 1:
            if expression == '.':
                for leftpntr in range(0,len(s)):
                    expression_options.append((leftpntr, leftpntr+1))
            else:
                for 


            # Then we know it's a 0 or many



print(isMatch("ab", 'ab'))
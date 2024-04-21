from typing import List

def isValid(s: str) -> bool:

    closers: dict = {')': '(',
                     ']': '[',
                     '}': '{'}

    stack: list[str] = []

    for character in s:
        if len(stack) == 0:
            stack.append(character)
        else:
            latest_char: str = stack[-1]

            # Get opener if it exists.
            opener = closers.get(character, None)

            if opener == latest_char:
                stack.pop()
            else:
                stack.append(character)
    return len(stack) == 0


print(isValid("()[]{}"))
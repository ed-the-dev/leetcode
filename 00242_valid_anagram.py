from typing import List

def isAnagram(s: str, t: str) -> bool:

    char_list = list(s)

    for character in t:
        if character in char_list:
            char_list.remove(character)
        else:
            return False
        
    if len(char_list) == 0:
        return True
    return False

# Or make two dicts from the strings. If the dicts are equal then True, else False

print(isAnagram('man', 'nam'))
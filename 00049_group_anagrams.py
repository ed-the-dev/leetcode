from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    # make a dictionary of dictionaries, where the key is a dict, and the value is the word.

    anagrams_words: dict = {}


    for word in strs:
        # Create dict

        anagram: dict = {}

        # for letter in word:
        #     if letter in anagram:
        #         anagram[letter] += 1
        #     else:
        #         anagram[letter] = 1

        # anagram_key = tuple(dict(sorted(anagram.items())).items())

        anagram_key = ''.join(sorted(word))

        # Or I can build a key from just sorting the word, and making into a string.

        if anagram_key in anagrams_words.keys():
            anagrams_words[anagram_key].append(word)
        else:
            anagrams_words[anagram_key] = [word]


        # this is a nice way of adding stuff to a dict.
        # d[anagram_key] = d.get(anagram_key,list()) + [word]

    result = []

    for value in anagrams_words.values():
        result.append(value)

    return result
        




print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
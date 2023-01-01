# @author: yprakash

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dct = {}
        s = s.split()
        if len(s) != len(pattern):
            return False

        for letter, word in zip(pattern, s):
            if letter in dct:
                if dct[letter] != word:
                    return False
            elif word in dct.values():
                return False
            else:
                dct[letter] = word

        return True

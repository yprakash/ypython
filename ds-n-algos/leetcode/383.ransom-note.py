# @author: yprakash
from collections import Counter


class Solution(object):
    # https://leetcode.com/submissions/detail/783220021/
    def canConstruct(self, ransomNote, magazine):
        count = Counter(magazine)
        for c in ransomNote:
            if c not in count or count[c] < 1:
                return False
            count[c] -= 1

        return True

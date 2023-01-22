# @author: yprakash
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/submissions/882896667/

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return s == target or ('1' in s and '1' in target)

# @author: yprakash
# https://leetcode.com/problems/add-binary/submissions/897591272/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))

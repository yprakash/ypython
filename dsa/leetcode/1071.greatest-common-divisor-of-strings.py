# @author: yprakash
from math import gcd


# https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/889086033/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1), len(str2))]
        return ''

# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/804080816/
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        snums2 = ''.join([chr(x) for x in nums2])
        strmax = ''
        maxlen = 0

        for num in nums1:
            strmax += chr(num)
            if strmax in snums2:
                if maxlen < len(strmax):
                    maxlen = len(strmax)
            else:
                strmax = strmax[1:]

        return maxlen

# @author: yprakash
# Problem: RLE- Run Length Encoding
# Constraints: 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol
# must only use constant extra space
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/822695503/
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            count, j = 1, i + 1

            while j < len(chars) and chars[j] == chars[i]:
                count += 1
                j += 1

            i += 1
            if count < 2:
                continue
            for d in str(count):
                chars[i] = d
                i += 1
            while i < j:
                del chars[i]
                j -= 1

        return len(chars)

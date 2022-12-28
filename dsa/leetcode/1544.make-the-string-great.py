# @author: yprakash
from collections import deque


class Solution:
    # https://leetcode.com/submissions/detail/839058355/
    def makeGood(self, s: str) -> str:
        stack = deque()

        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:  # 'a'=97 - 'A'=65
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)

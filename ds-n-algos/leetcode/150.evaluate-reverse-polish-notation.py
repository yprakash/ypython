# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/860909156/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = ['+', '-', '*', '/']
        for t in tokens:
            if t in operators:
                n2 = stack.pop()
                n1 = stack.pop()
                if t == '+':
                    t = n1 + n2
                elif t == '-':
                    t = n1 - n2
                elif t == '*':
                    t = n1 * n2
                else:
                    t = int(n1 / n2)

            stack.append(int(t))

        return stack.pop()

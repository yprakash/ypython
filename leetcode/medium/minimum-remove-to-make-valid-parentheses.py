# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/731102663/
    def minRemoveToMakeValid(self, s):
        s = list(s)
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:  # Remove this char if there is no matching brace
                    s[i] = 0  # or ''

        for i in stack:
            s[i] = 0  # or ''

        return ''.join([x for x in s if x])

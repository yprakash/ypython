# @author: yprakash
# Given a string s (consists of parentheses only '()[]{}'), determine if it is valid or not.

class Solution(object):
    # https://leetcode.com/submissions/detail/731044033/
    def isValid(self, s):
        stack = []
        mp = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in mp:  # If it is closing brace
                if not stack or stack.pop() != mp[c]:
                    return False
            else:
                stack.append(c)

        return False if stack else True

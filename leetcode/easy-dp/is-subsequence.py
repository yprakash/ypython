# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739408203/
    def isSubsequence(self, s, t):
        i = 0
        n = len(t)

        for c in s:
            while i < n and t[i] != c:
                i += 1
            if i == n:
                return False
            i += 1

        return True


obj = Solution()
print(obj.isSubsequence("", ""))  # true
print(obj.isSubsequence("aec", "abcde"))  # false
print(obj.isSubsequence("ace", "abcde"))  # true
print(obj.isSubsequence("abc", "ahbgdc"))  # true
print(obj.isSubsequence("axc", "ahbgdc"))  # false
print(obj.isSubsequence("aaaaaa", "bbaaaa"))  # false

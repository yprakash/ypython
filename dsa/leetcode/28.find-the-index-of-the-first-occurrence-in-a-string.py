# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/837272607/
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # https://leetcode.com/submissions/detail/837277601/
    def strStr2(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            found = True

            for j, c in enumerate(needle):
                if i+j >= len(haystack) or c != haystack[i + j]:
                    found = False
                    break
            if found:
                return i

        return -1

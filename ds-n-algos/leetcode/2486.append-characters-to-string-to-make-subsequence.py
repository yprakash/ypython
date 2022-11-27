# @author: yprakash

class Solution:
    # https://leetcode.com/contest/weekly-contest-321/submissions/detail/850407891/
    def appendCharacters(self, s: str, t: str) -> int:
        ti = 0
        for si, sc in enumerate(s):
            if t[ti] == sc:
                ti += 1
                if ti == len(t):
                    return 0

        return len(t) - ti

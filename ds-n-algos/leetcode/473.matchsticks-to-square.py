# @author: yprakash
from functools import lru_cache
from typing import List


class Solution(object):
    # DFS + cache recursion
    # https://leetcode.com/submissions/detail/744829151/
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        if n < 4:
            return False
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        s = s // 4
        matchsticks.sort(reverse=True)

        @lru_cache(maxsize=None)
        def find_edge(i, s1, s2, s3, s4):
            nonlocal s
            if i >= len(matchsticks):
                return s == s1 == s2 == s3 == s4
            if s1 > s or s2 > s or s3 > s or s4 > s:
                return False
            return find_edge(i + 1, s1 + matchsticks[i], s2, s3, s4) or \
                   find_edge(i + 1, s1, s2 + matchsticks[i], s3, s4) or \
                   find_edge(i + 1, s1, s2, s3 + matchsticks[i], s4) or \
                   find_edge(i + 1, s1, s2, s3, s4 + matchsticks[i])

        return find_edge(0, 0, 0, 0, 0)

    # 	Time Limit Exceeded using Recursion https://leetcode.com/submissions/detail/744814765/
    def recurse(self, matchsticks, index, a, b, c, d):
        # a,b,c,d are four sides of square
        if index == len(matchsticks):  # base case
            return a == 0 and b == 0 and c == 0 and d == 0

        # we should explore for all sides for given index
        if matchsticks[index] <= a:
            a -= matchsticks[index]
            if self.recurse(matchsticks, index + 1, a, b, c, d):
                return True
            a += matchsticks[index]

        if matchsticks[index] <= b:
            b -= matchsticks[index]
            if self.recurse(matchsticks, index + 1, a, b, c, d):
                return True
            b += matchsticks[index]

        if matchsticks[index] <= c:
            c -= matchsticks[index]
            if self.recurse(matchsticks, index + 1, a, b, c, d):
                return True
            c += matchsticks[index]

        if matchsticks[index] <= d:
            d -= matchsticks[index]
            if self.recurse(matchsticks, index + 1, a, b, c, d):
                return True
            d += matchsticks[index]

        return False

    def makesquare2(self, matchsticks):
        n = len(matchsticks)
        if n < 4:
            return False
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        s = s // 4
        a, b, c, d = s, s, s, s
        return self.recurse(matchsticks, 0, a, b, c, d)

    # https://leetcode.com/submissions/detail/744792441/
    # inCorrect 0-1 knapsack like DP solution
    def makesquare3(self, matchsticks):
        n = len(matchsticks)
        if n < 4:
            return False
        s = sum(matchsticks)
        if s % 4 != 0:
            return False

        s = int(s / 2)
        dp1 = [False] * (1 + s)
        dp1[0] = True

        for i in range(1, n):
            dp2 = [False] * (1 + s)
            dp2[0] = True
            for j in range(1, 1 + s):
                if j - matchsticks[i] >= 0 and dp1[j - matchsticks[i]]:
                    dp2[j] = True
                elif dp1[j]:
                    dp2[j] = True

            dp1 = dp2
            print(dp1)
        return dp1[s] and dp1[int(s / 2)]


nums = [
    [1, 1, 2, 2, 2],  # true
    [2, 2, 2, 2, 2, 6],  # False
    [7215807,6967211,5551998,6632092,2802439,821366,2465584,9415257,8663937,3976802,2850841,803069,2294462,8242205,9922998],
    [1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755]
]
obj = Solution()
for num in nums:
    print(obj.makesquare(num))

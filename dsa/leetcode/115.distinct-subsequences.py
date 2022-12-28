# @author: yprakash
from functools import lru_cache


class Solution:
    # Using memoization
    # https://leetcode.com/submissions/detail/838728778/
    def numDistinct1(self, s: str, t: str) -> int:
        @lru_cache(None)
        def distinct(m, n):
            if n < 0:
                return 1
            if m < 0:
                return 0

            if s[m] == t[n]:
                return distinct(m-1, n-1) + distinct(m-1, n)
            return distinct(m-1, n)

        return distinct(len(s)-1, len(t)-1)

    # https://leetcode.com/submissions/detail/838806549/
    # Bottom Up Tabulation
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for j in range(n+1):
            dp[0][j] = 0  # If first string is empty
        for i in range(m+1):
            dp[i][0] = 1  # If second string is empty

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    # If last characters are same, 1. ignore last character of first string
                    # 2. consider last characters of both strings in solution
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # ignore last character of first string
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


if __name__ == "__main__":
    testcases = [
        ["rabbbit", "rabbit"],  # 3
        ["babgbag", "bag"],  # 5
    ]
    for ss, tt in testcases:
        obj = Solution()
        print(obj.numDistinct(ss, tt))

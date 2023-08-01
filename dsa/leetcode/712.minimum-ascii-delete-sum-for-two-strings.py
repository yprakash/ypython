# @author: yprakash
class Solution:
    # https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/submissions/1008545657/
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[-1] * (1 + len(s2)) for _ in range(1 + len(s1))]
        return self.solve(s1, s2, 0, 0, dp)

    def solve(self, s1, s2, i, j, dp):
        if dp[i][j] > -1:
            return dp[i][j]

        if i == len(s1):
            return sum(ord(ch) for ch in s2[j:])
        if j == len(s2):
            return sum(ord(ch) for ch in s1[i:])
        nt = min(ord(s1[i]) + self.solve(s1, s2, i + 1, j, dp), ord(s2[j]) + self.solve(s1, s2, i, j + 1, dp))
        tk = float('inf')
        if s1[i] == s2[j]:
            tk = self.solve(s1, s2, i + 1, j + 1, dp)
        dp[i][j] = min(nt, tk)
        return dp[i][j]

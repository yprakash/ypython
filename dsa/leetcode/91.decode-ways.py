# @author: yprakash

class Solution(object):
    def is_valid_str2(self, s, i):
        if s[i] == '1' or (s[i] == '2' and s[i + 1] in ('0', '1', '2', '3', '4', '5', '6')):
            return True
        return False

    # https://leetcode.com/submissions/detail/812467141/
    def numDecodings(self, s):
        if s[0] == '0' or '00' in s:
            return 0
        if len(s) == 1:
            return 1
        if s[1] == '0' and s[0] not in ('1', '2'):
            return 0
        if len(s) == 2:
            return 2 if s[1] != '0' and self.is_valid_str2(s, 0) else 1

        dp = [0] * len(s)
        dp[0] = 1
        dp[1] = 2 if s[1] != '0' and self.is_valid_str2(s, 0) else 1
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i-1] not in ('1', '2'):
                    return 0
                dp[i] = dp[i-2]
            elif self.is_valid_str2(s, i-1):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        return dp[-1]


if __name__ == "__main__":
    testcases = [
        "30",  # 0
        "301",  # 0
        "230",  # 0
        "10",  # 1
        "10011",  # 0
        "207",  # 1
    ]
    for testcase in testcases:
        obj = Solution()
        print(testcase, obj.numDecodings(testcase))

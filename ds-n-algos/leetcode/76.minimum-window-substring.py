# @author: yprakash
import math
from collections import Counter


class Solution:
    # faster than 94.05% of Python3 online submissions as on 20221022
    # https://leetcode.com/submissions/detail/827694188/

    def minWindow(self, s: str, t: str) -> str:
        if t in s:
            return t
        m = len(s)
        if len(t) <= 1 or m < len(t):
            return ""

        # Use two pointers to create a window of letters in s, which would have all the characters from t.
        s_freq, t_cntr = {}, Counter(t)
        t_uniq = len(t_cntr)
        ans, ans_len = "", math.inf
        left, right, matches = 0, 0, 0

        while right < m:
            # Expand the right pointer until all the characters of t are covered.
            while right < m:
                s_freq[s[right]] = 1 + s_freq.get(s[right], 0)
                if s_freq[s[right]] == t_cntr.get(s[right], 0):
                    matches += 1
                    if matches == t_uniq:
                        break

                right += 1
            if right == m:
                return ans

            # Once all the characters are covered, move the left pointer and ensure that
            # all the characters are still covered to minimize the subarray size.
            while left <= right:
                if s_freq[s[left]] == t_cntr.get(s[left], 0):
                    matches -= 1
                s_freq[s[left]] -= 1
                if s[left] in t_cntr and s_freq[s[left]] < t_cntr[s[left]]:
                    break
                left += 1

            # Now s[left: right+1] contains all t's chars
            if ans_len > 1 + right - left:
                ans_len = 1 + right - left
                ans = s[left: right+1]

            # Continue expanding the right and left pointers until you reach the end of s.
            left += 1
            right += 1

        return ans


if __name__ == "__main__":
    testcases = [
        ("a", "a"),  # "a"
        ("a", "aa"),  # ""
        ("abc", "cba"),  # "abc"
        ("ADOBECODEBANC", "ABC"),  # "BANC"
    ]
    for ss, tt in testcases:
        obj = Solution()
        print(obj.minWindow(ss, tt))

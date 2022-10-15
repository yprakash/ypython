# @author: yprakash
import math
import sys
from collections import defaultdict
from functools import lru_cache


class Solution:
    # Constraints: 1 <= len(s) <= 100 and 0 <= k <= s.length
    # https://leetcode.com/submissions/detail/822894464/
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def get_length(freq):
            if freq <= 1:
                return 1  # only the character without appending 1
            if freq < 10:
                return 2
            if freq < 100:
                return 3
            return 4  # From given constraint

        n = len(s)

        @lru_cache(None)
        def compression(start, k):
            if k < 0:
                return math.inf
            if start == n or n - start <= k:
                return 0

            most_freq, ans = 0, sys.maxsize
            counts = defaultdict(int)

            for i in range(start, n):
                # The strategy is divide s[start:] into two halves (upto i and after i)
                # Find out most frequent elem in left half and remove all other elements
                # Recurse for right half with k -= no.of removed elements in left half
                counts[s[i]] += 1
                if most_freq < counts[s[i]]:
                    most_freq = counts[s[i]]
                    ans = min(ans,
                              get_length(most_freq) + compression(i+1, k - (i - start + 1 - most_freq)))

            return ans

        return compression(0, k)


if __name__ == "__main__":
    testcases = [
        [1, "a"],  # 0 ""
        [2, "aabbaa"],  # 2 "a4"
        [2, "aaabcccd"],  # 4 "a3c3"
        [0, "aaaaaaaaaaa"],  # 3 "a11"
    ]
    for kk, s2 in testcases:
        obj = Solution()
        print(obj.getLengthOfOptimalCompression(s2, kk))

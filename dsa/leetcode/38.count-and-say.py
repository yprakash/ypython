# @author: yprakash
from functools import lru_cache


class Solution:
    # https://leetcode.com/submissions/detail/824840116/
    def countAndSay(self, n: int) -> str:
        @lru_cache(maxsize=None)
        def count_rec(x):
            if x <= 1:
                return "1"

            s = count_rec(x-1)
            ans = ""
            r = iter(range(len(s)))
            j = next(r, None)

            while j is not None:
                i, count = j, 0
                while j is not None and s[i] == s[j]:
                    count += 1
                    j = next(r, None)
                ans += str(count) + s[i]
            return ans

        return count_rec(n)


if __name__ == "__main__":
    for k in range(1, 10):
        obj = Solution()
        print(obj.countAndSay(k))

# @author: yprakash

from functools import lru_cache, reduce
from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        def next_term(s):
            return "".join(f"{len(list(group))}{ch}" for ch, group in groupby(s))

        # functools.reduce(function, iterable, initializer) takes an iterable and reduces it to a single value by
        # applying the function cumulatively. lambda takes 2 arguments: accumulator: the result so far, starts as '1'
        # _: the current item in the iterable (in this case, we ignore it)
        return reduce(lambda acc, _: next_term(acc), range(n - 1), '1')

class Solution2:
    def countAndSay(self, n: int) -> str:
        data = '1'
        for _ in range(1, n):
            data = "".join(f"{len(list(group))}{ch}" for ch, group in groupby(data))
        return data


class Solution1:
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

# @author: yprakash
from collections import Counter
from typing import List


# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/892057581/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pc = Counter(p)
        sc = Counter(s[:len(p) - 1])

        for i, (x, y) in enumerate(zip(s, s[len(p) - 1:])):
            if y not in sc:
                sc[y] = 1
            else:
                sc[y] += 1
            if sc == pc:
                res.append(i)
            sc[x] -= 1
            if sc[x] == 0:
                del sc[x]

        return res


if __name__ == "__main__":
    testcases = [
        ("abab", "ab"),  # [0, 1, 2]
        ("cbaebabacd", "abc"),  # [0, 6]
    ]
    for s1, p1 in testcases:
        obj = Solution()
        print(obj.findAnagrams(s1, p1))

# @author: yprakash
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/naming-a-company/submissions/894399260/
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0
        prefix_map = [set() for _ in range(26)]
        for idea in ideas:
            prefix_map[ord(idea[0]) - ord('a')].add(idea[1:])

        for i in range(25):
            for j in range(i + 1, 26):
                common = len(prefix_map[i] & prefix_map[j])
                ans += 2 * (len(prefix_map[i]) - common) * (len(prefix_map[j]) - common)

        return ans


# https://leetcode.com/problems/naming-a-company/submissions/894388964/
# InCorrect
class Solution2:
    def distinctNames(self, ideas: List[str]) -> int:
        prefix_map = defaultdict(int)
        suffix_map = defaultdict(list)
        for idea in ideas:
            prefix_map[idea[0]] += 1
            suffix_map[idea[1:]].append(idea[0])

        names, n = 0, len(ideas)
        for v in suffix_map.values():
            names += n - len(v)

        for v in prefix_map.values():
            if v > 1:
                names -= v * (v - 1)
        return names


if __name__ == "__main__":
    testcases = [
        ["lack", "back"],  # 0
        ["coffee", "donuts", "time", "toffee"],  # 6
        ["alrgtxxdj", "illqfngl", "rlrgtxxdj"],  # 4
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.distinctNames(testcase))

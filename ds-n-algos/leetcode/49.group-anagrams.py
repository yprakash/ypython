# @author: yprakash
from collections import defaultdict, Counter
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/831758450/
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_strs = defaultdict(list)

        for s in strs:
            key = list(Counter(s).items())  # List of character frequencies
            # (('a', 1), ('b', 2)) is different from (('b', 2), ('a', 1)). So we should sort
            key.sort()
            # Lists or dicts can't be used as keys, can't hashable
            counter_to_strs[tuple(key)].append(s)

        return list(counter_to_strs.values())


if __name__ == "__main__":
    testcases = [
        [""],  # [[""]]
        ["a"],  # [["a"]]
        ["eat", "tea", "tan", "ate", "nat", "bat"],  # [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.groupAnagrams(testcase))

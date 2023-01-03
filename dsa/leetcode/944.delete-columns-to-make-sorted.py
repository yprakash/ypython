# @author: yprakash
from typing import List


# https://leetcode.com/problems/delete-columns-to-make-sorted/submissions/870158984/
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = [''.join(s) for s in zip(*strs)]
        return len(strs) - sum(
            all(a <= b for a, b in zip(s, s[1:]))
            for s in strs)


if __name__ == "__main__":
    testcases = [
        ["a", "b"],  # 0
        ["abc", "bce", "cae"],  # 1
        ["cba", "daf", "ghi"],  # 1
        ["zyx", "wvu", "tsr"],  # 3
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.minDeletionSize(testcase))

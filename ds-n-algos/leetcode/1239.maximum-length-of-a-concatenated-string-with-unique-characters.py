# @author: yprakash
from typing import List


class Solution:
    # Runtime: 80 ms, faster than 98.45% of Python3 submissions
    # https://leetcode.com/submissions/detail/829001627/
    def maxLength(self, arr: List[str]) -> int:
        def recurse(prefix, index):
            if index == len(arr):  # Came to end
                return len(prefix)
            if len(set(arr[index])) < len(arr[index]):
                # arr[index] has duplicate characters
                return recurse(prefix, index + 1)

            for char in arr[index]:
                if char in prefix:
                    # arr[index] can't be appended to prefix
                    return recurse(prefix, index + 1)

            return max(recurse(prefix, index + 1),  # without arr[index]
                       recurse(prefix + arr[index], index + 1))

        return recurse('', 0)


if __name__ == "__main__":
    testcases = [
        ["aa", "bb"],  # 0
        ["un", "iq", "ue"],  # 4
        ["cha", "r", "act", "ers"],  # 6
        ["abcdefghijklmnopqrstuvwxyz"],  # 26
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.maxLength(testcase))

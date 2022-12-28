# @author: yprakash
from collections import Counter
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/836238435/
    # A palindrome must be mirrored over the center. If we prepend the word "ab" on the left,
    # We must append "ba" on the right to keep it a palindrome.
    def longestPalindrome(self, words: List[str]) -> int:
        longest = 0
        middle = False
        occs = Counter(words)

        for word, freq in occs.items():
            if word[0] == word[1]:
                # We can use exactly one in the middle to form an even longer palindrome.
                if freq % 2 == 1:
                    middle = True
                    longest += freq - 1
                else:
                    longest += freq
            else:
                rev = word[1] + word[0]
                longest += min(freq, occs.get(rev, 0))

        if middle:
            longest += 1
        longest *= 2
        return longest


if __name__ == "__main__":
    testcases = [
        ["ll", "lb", "bb"],  # 2
        ["cc", "ll", "xx"],  # 2
        ["lc", "cl", "gg"],  # 6
        ["ab", "ty", "yt", "lc", "cl", "ab"],  # 8
        ["nn", "nn", "hg", "gn", "nn", "hh", "gh", "nn", "nh", "nh"],  # 14
        ["qo", "fo", "fq", "qf", "fo", "ff", "qq", "qf", "of", "of", "oo", "of", "of", "qf", "qf", "of"],  # 14
        # ["qo", "fo", "ff", "qq", "qf", "of", "of", "oo", "of", "qf", "qf", "of"],  # 14
        ["ll", "lb", "bb", "bx", "xx", "lx", "xx", "lx", "ll", "xb", "bx", "lb", "bb", "lb", "bl", "bb", "bx", "xl",
         "lb", "xx"],  # 26
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.longestPalindrome(testcase))

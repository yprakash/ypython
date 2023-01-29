# @author: yprakash
from typing import List


# https://leetcode.com/problems/concatenated-words/submissions/887113519/
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dp = set()
        dit = set(words)
        mini = len(min(words, key=lambda s: len(s)))

        def can(word):
            if word in dp:
                return True

            for i in range(mini, len(word)):
                left, right = word[:i], word[i:]
                if left in dit:
                    if right in dit or can(right):
                        dp.add(word)
                        return True
            return False

        return [w for w in words if can(w)]


if __name__ == "__main__":
    testcases = [
        ["cat", "catdog", "dog"],  # ["catdog"]
        ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
        # ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
    ]
    with open('472.concatenated-words-input.txt') as f:
        lines = f.read().splitlines()
        testcases.append(eval(lines[0]))
    for testcase in testcases:
        obj = Solution()
        print(obj.findAllConcatenatedWordsInADict(testcase))

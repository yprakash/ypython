# @author: yprakash
from typing import List


class TrieNode:
    def __init__(self, end_of_word=False):
        self.children = {}
        self.end_of_word = end_of_word


# https://leetcode.com/problems/concatenated-words/submissions/887424440/
class Solution:
    def trie_insert(self, node, word):
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dp = {}
        root = TrieNode()
        for w in words:
            self.trie_insert(root, w)

        def concatenated(word, index=0):
            node = root
            i = index

            while i < len(word):
                if node.end_of_word:
                    if word[i:] not in dp:
                        dp[word[i:]] = concatenated(word, i)
                    if dp[word[i:]]:
                        return True

                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                i += 1

            return index > 0 and node.end_of_word

        return [w for w in words if concatenated(w)]


# TLE https://leetcode.com/problems/concatenated-words/submissions/887119717/
class Solution1:
    def trie_insert(self, node, word):
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            self.trie_insert(root, w)

        def concatenated(word, index=0):
            node = root
            i = index

            while i < len(word):
                if node.end_of_word:
                    if concatenated(word, i):
                        return True

                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                i += 1

            return index > 0 and node.end_of_word

        return [w for w in words if concatenated(w)]


# TLE https://leetcode.com/problems/concatenated-words/submissions/887113519/
class Solution2:
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

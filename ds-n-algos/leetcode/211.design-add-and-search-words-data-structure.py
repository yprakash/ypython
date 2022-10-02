# @author: yprakash

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


# https://leetcode.com/submissions/detail/813464065/
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word):
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.end_of_word
            # End of inner def dfs

        return dfs(0, self.root)

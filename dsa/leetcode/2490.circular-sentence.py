# @author: yprakash

class Solution:
    # https://leetcode.com/contest/weekly-contest-322/submissions/detail/854215927/
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False

        words = sentence.split()
        for w1, w2 in zip(words, words[1:]):
            if w1[-1] != w2[0]:
                return False

        return True

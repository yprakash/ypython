# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/824607867/
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

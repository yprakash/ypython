# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/805707793/
    def reverseWords(self, s):
        delim = ' '
        words = s.split(delim)
        for i in range(len(words)):
            words[i] = words[i][::-1]

        return delim.join(words)

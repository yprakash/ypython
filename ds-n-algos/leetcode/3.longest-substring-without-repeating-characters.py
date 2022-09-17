# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/802109689/
    # O(N) sliding window
    def lengthOfLongestSubstring(self, s):
        map = {}
        left, longest = 0, 0

        for right, char in enumerate(s):
            if char in map and map[char] >= left:
                left = map[char] + 1
            elif longest < 1 + right - left:
                longest = 1 + right - left
            map[char] = right

        return longest

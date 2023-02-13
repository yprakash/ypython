# @author: yprakash
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/submissions/897067308/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (1 + high) // 2 - low // 2

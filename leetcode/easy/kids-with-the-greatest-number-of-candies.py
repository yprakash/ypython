# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/704954208/
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = max(candies)
        return [candy + extraCandies >= n for candy in candies]
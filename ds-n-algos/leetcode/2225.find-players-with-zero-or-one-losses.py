from collections import Counter
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/851324537/
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {w for w, l in matches}
        losers = Counter([l for w, l in matches])
        ans0, ans1 = [], []

        for winner in winners:
            if winner not in losers:
                ans0.append(winner)
        for loser in losers:
            if losers[loser] == 1:
                ans1.append(loser)

        ans0.sort()
        ans1.sort()
        return [ans0, ans1]

# @author: yprakash
from typing import List


# https://leetcode.com/problems/best-team-with-no-conflicts/submissions/888435599/
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores = [s for a, s in sorted(zip(ages, scores))]
        msis = scores.copy()

        for i in range(1, len(scores)):
            for j in range(i):
                if scores[j] <= scores[i]:
                    msis[i] = max(msis[i], msis[j] + scores[i])
        return max(msis)

# @author: yprakash
from typing import List


# https://leetcode.com/problems/longest-subsequence-with-limited-sum/submissions/865314075/
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = [0] * len(queries)
        queries = [(q, j) for j, q in enumerate(queries)]
        queries.sort()

        s, i, j = 0, 0, 0
        while i < len(nums) and j < len(queries):
            if s <= queries[j][0]:
                s += nums[i]
                i += 1
            else:
                answer[queries[j][1]] = i - 1
                j += 1

        while j < len(queries):
            if s <= queries[j][0]:
                answer[queries[j][1]] = i
            else:
                answer[queries[j][1]] = i - 1
            j += 1

        return answer

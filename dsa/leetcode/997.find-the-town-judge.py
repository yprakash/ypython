# @author: yprakash
from collections import defaultdict


class Solution(object):
    # https://leetcode.com/submissions/detail/738974957/
    def findJudge(self, n, trust):
        if n <= 1:
            return 1
        inbound = defaultdict(int)  # used to track how many persons are trusting in him
        outbound = defaultdict(int)  # used to track how many persons he is trusting

        for node in trust:
            outbound[node[0]] += 1
            inbound[node[1]] += 1

        for key, value in inbound.items():
            if value == n-1:  # if all others are trusting him
                if outbound[key] == 0:  # if he trusts NO one
                    return key

        return -1

    # https://leetcode.com/submissions/detail/738953241/
    def findJudge2(self, n, trust):
        judge = [True] * (n+1)
        judge[0] = False
        for t in trust:
            judge[t[0]] = False

        label = 0
        for i, j in enumerate(judge):
            if j:
                if label:
                    return -1
                label = i

        for t in trust:
            if t[1] == label:
                judge[t[0]] = True

        judge.pop(0)
        return label if all(judge) else -1


obj = Solution()
print(obj.findJudge(2, [[1, 2]]))  # 2
print(obj.findJudge(3, [[1, 3], [2, 3]]))  # 3
print(obj.findJudge(3, [[1, 2], [2, 3]]))  # -1
print(obj.findJudge(3, [[1, 3], [2, 3], [3, 1]]))  # -1

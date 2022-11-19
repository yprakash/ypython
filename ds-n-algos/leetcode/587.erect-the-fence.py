# @author: yprakash
from typing import List, Set, Tuple


class Solution:
    # https://leetcode.com/submissions/detail/846137323/
    def outerTrees(self, trees: List[List[int]]) -> Set[Tuple[int, int]]:
        def direction(p, q, r):
            return (p[0] - r[0]) * (q[1] - r[1]) - (p[1] - r[1]) * (q[0] - r[0])

        if len(trees) <= 3:
            return trees

        trees = [(p[0], p[1]) for p in trees]
        trees.sort()
        lower, upper = [], []

        for point in trees:
            while len(lower) >= 2 and direction(lower[-2], lower[-1], point) < 0:
                lower.pop()
            lower.append(point)

        for point in reversed(trees):
            while len(upper) >= 2 and direction(upper[-2], upper[-1], point) < 0:
                upper.pop()
            upper.append(point)

        return set(upper[1:] + lower[1:])

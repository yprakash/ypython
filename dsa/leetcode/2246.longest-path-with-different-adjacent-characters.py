# @author: yprakash
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/submissions/877323802/
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        answer = 1
        graph = defaultdict(list)  # build the graph

        for i, p in enumerate(parent):
            if i:
                graph[p].append(i)

        def dfs(node):
            nonlocal answer
            longest = second_longest = 0

            for child in graph[node]:
                path_length = dfs(child)
                if s[child] != s[node]:
                    if path_length > longest:
                        second_longest = longest
                        longest = path_length
                    elif path_length > second_longest:
                        second_longest = path_length

            answer = max(answer, longest + second_longest + 1)
            return longest + 1

        dfs(0)
        return answer

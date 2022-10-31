# @author: yprakash
# https://leetcode.com/contest/weekly-contest-317/submissions/detail/833094454/
from typing import List


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        popular = []
        creator_views = {}

        for creator, i, view in zip(creators, ids, views):
            if creator in creator_views:
                tmp = creator_views[creator]
                tmp[0] += view
                if tmp[1] == view:
                    tmp[2].append(i)
                elif tmp[1] < view:
                    tmp[1] = view
                    tmp[2] = [i]
            else:
                tmp = [view, view, [i]]

            creator_views[creator] = tmp

        max_view = 0
        for creator, value in creator_views.items():
            if value[0] > max_view:
                popular = [creator]
                max_view = value[0]
            elif value[0] == max_view:
                popular.append(creator)

        return [[creator, min(creator_views[creator][2])] for creator in popular]

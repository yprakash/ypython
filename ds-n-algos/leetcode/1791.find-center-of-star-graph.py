# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739003117/
    def findCenter(self, edges):
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


obj = Solution()
print(obj.findCenter([[1,2], [2,3], [4,2]]))  # 2
print(obj.findCenter([[1,2], [5,1], [1,3], [1,4]]))  # 1

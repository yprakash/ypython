# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739219145/
    def getRow(self, rowIndex):
        if rowIndex <= 0:
            return [1]
        curr = [1, 1]

        while len(curr) <= rowIndex:
            prev = curr
            curr = [1]
            curr.extend([a + b for a, b in zip(prev, prev[1:])])
            curr.append(1)

        return curr


obj = Solution()
for i in range(10):
    print(obj.getRow(i))

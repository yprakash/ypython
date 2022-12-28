# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739133626/
    def generate(self, numRows):
        if numRows <= 1:
            return [[1]]
        res = [[1], [1, 1]]

        while len(res) < numRows:
            row = [1]
            row.extend([a + b for a, b in zip(res[-1], res[-1][1:])])
            row.append(1)
            res.append(row)
        return res


obj = Solution()
for i in range(1, 31):
    print(obj.generate(i))

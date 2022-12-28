# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/736251416/
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts.sort()
        horizontalCuts.append(h)
        hmax = horizontalCuts[0]
        for x, y in zip(horizontalCuts, horizontalCuts[1:]):
            hmax = max(y-x, hmax)

        verticalCuts.sort()
        verticalCuts.append(w)
        vmax = verticalCuts[0]
        for x, y in zip(verticalCuts, verticalCuts[1:]):
            vmax = max(y-x, vmax)

        return (hmax * vmax) % 1000000007

    # https://leetcode.com/submissions/detail/736249604/
    def maxArea2(self, h, w, horizontalCuts, verticalCuts):
        verticalCuts.append(0)
        verticalCuts.sort()
        verticalCuts.append(w)

        horizontalCuts.append(0)
        horizontalCuts.sort()
        horizontalCuts.append(h)

        h = max([y - x for x, y in zip(horizontalCuts, horizontalCuts[1:])])
        v = max([y - x for x, y in zip(verticalCuts, verticalCuts[1:])])
        return (h * v) % 1000000007


obj = Solution()
print(obj.maxArea(5, 4, [1, 2, 4], [1, 3]))
print(obj.maxArea(5, 4, [3, 1], [1]))
print(obj.maxArea(5, 4, [3], [3]))

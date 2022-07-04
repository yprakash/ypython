# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/736110328/
    def maximumUnits(self, boxTypes, truckSize):
        units = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        for box in boxTypes:
            mn = min(box[0], truckSize)
            units += mn * box[1]
            truckSize -= mn
            if truckSize <= 0:
                break
        return units

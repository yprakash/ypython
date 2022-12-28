# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/800140381/
    def findOriginalArray(self, changed):
        res = []
        if len(changed) < 2 or len(changed) % 2 != 0:
            return res

        seen = [False] * len(changed)
        changed.sort()
        i, j = 0, 1  # Two pointer approach

        while j < len(changed):
            while i < j and seen[i]:
                i += 1
            if j <= i:
                j = i + 1
            while j < len(changed) and changed[j] < 2 * changed[i]:
                j += 1
            if j == len(changed) or changed[j] > 2 * changed[i]:
                return []

            res.append(changed[i])
            seen[j] = True
            j += 1
            i += 1

        return res if len(res) * 2 == len(changed) else []


if __name__ == '__main__':
    testcases = [
        [1], # []
        [0, 0, 0, 0], # [0, 0]
        [2, 4, 3, 2], # []
        [6, 3, 0, 1], # []
        [1, 3, 4, 2, 6, 8], # [1, 3, 4]
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.findOriginalArray(testcase))

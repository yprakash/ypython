# @author: yprakash
from bisect import bisect_left


class Solution(object):
    # https://leetcode.com/submissions/detail/811186977/
    def findClosestElements(self, arr, k, x):
        right = bisect_left(arr, x)
        left = right - 1
        count = 0
        while count < k:
            if left < 0:
                right += k - count
                break
            if right >= len(arr):
                left -= k - count
                break

            a, b = arr[left], arr[right]
            if abs(a-x) < abs(b-x) or (a < b and abs(a-x) == abs(b-x)):
                left -= 1
            else:
                right += 1
            count += 1

        return arr[left+1:right]


if __name__ == "__main__":
    testcases = [
        [[1, 2, 3, 4, 5], 4, 3],  # [1, 2, 3, 4]
        [[1, 2, 3, 4, 5], 4, -1],  # [1, 2, 3, 4]
        [[1, 1, 1, 10, 10, 10], 1, 9],  # [10]
    ]
    for ar, k, x in testcases:
        obj = Solution()
        print(obj.findClosestElements(ar, k, x))

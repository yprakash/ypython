# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/756570807/
    def searchMatrix(self, matrix, target):
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            if target < matrix[row][col]:
                col -= 1
            else:
                row += 1

        return False


testcases = [
    [[[1]], [2]],  # False
    [[[1],
      [3]], [3]],  # True
    [[[1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
      ], [3, 11, 13]],  # True, True, False
]
for testcase in testcases:
    obj = Solution()
    for target in testcase[1]:
        print(obj.searchMatrix(testcase[0], target))

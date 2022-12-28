# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/786784310/
    def rotate(self, matrix: List[List[int]]) -> None:
        def swap(array):  # produces mirror image of the given 1D array
            left, right = 0, len(array) - 1
            while left < right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        # 1. symmetry the matrix: replace i-th row with i-th column
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. Swap each row
        for i in range(len(matrix)):
            swap(matrix[i])


if __name__ == "__main__":
    testcases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ]
    obj = Solution()
    for mat in testcases:
        obj.rotate(mat)
        print(mat)

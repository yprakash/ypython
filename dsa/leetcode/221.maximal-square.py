# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/801986875/
    def maximalSquare(self, matrix):
        for i in range(1, len(matrix)):
            matrix[i][0] = int(matrix[i][0])
        for j in range(len(matrix[0])):
            matrix[0][j] = int(matrix[0][j])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])

        return max([max(row) for row in matrix]) ** 2


if __name__ == "__main__":
    testcases = [
        [["0"]],  # 0
        [["0", "1"], ["1", "0"]],  # 1
        [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]],  # 4
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.maximalSquare(testcase))

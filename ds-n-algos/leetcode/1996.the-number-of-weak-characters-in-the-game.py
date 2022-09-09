# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/795478119/
    def numberOfWeakCharacters(self, properties):
        # Sort in descending order of attack power and ascending order of defense power
        properties.sort(key=lambda x: (-x[0], x[1]))
        weak = max_defense = 0

        for _, defense in properties:
            if defense < max_defense:
                weak += 1
            else:
                max_defense = defense

        return weak

    # https://leetcode.com/submissions/detail/795463494/
    # Naive O(N ^ 2) solution but Time Limit Exceeded
    def numberOfWeakCharacters1(self, properties):
        weak = 0
        properties.sort()

        for i in range(len(properties)-1):
            j = len(properties) - 1
            while properties[i][0] < properties[j][0]:
                if properties[i][1] < properties[j][1]:
                    weak += 1
                    break
                j -= 1

        return weak


if __name__ == "__main__":
    testcases = [
        [[5, 5], [6, 3], [3, 6]],  # 0
        [[2, 2], [3, 3]],  # 1
        [[1, 5], [10, 4], [4, 3]],  # 1
    ]
    obj = Solution()
    for testcase in testcases:
        print(obj.numberOfWeakCharacters(testcase))

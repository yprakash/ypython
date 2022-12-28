# @author: yprakash
# Given the integer array cardPoints and an integer k, return the maximum score you can obtain
# by choosing only k elements from either of extreme ends

class Solution(object):
    def display(self, k, cardPoints):
        print("Max when k= %d len=%d in %s: %d" % (k, len(cardPoints), cardPoints, self.maxScore(cardPoints, k)))

    # https://leetcode.com/submissions/detail/731521270/
    def maxScore(self, cardPoints, k):
        # initialize max_score as the sum of extreme k elements on the right side
        score = sum(cardPoints[-k:])
        max_score = score

        for i in range(k):
            # add an item from unseen left and subtract corresponding right element
            score += cardPoints[i] - cardPoints[i-k]
            if max_score < score:
                max_score = score

        return max_score

    # https://leetcode.com/submissions/detail/731495739/
    # Recursive Solution
    def maxScore2(self, cardPoints, k):
        return self.max_score(cardPoints, k, 0, len(cardPoints)-1)

    def max_score(self, cardPoints, k, left, right):
        if k < 1:  # shouldn't occur in ideal case
            return 0
        if k == 1:
            return max(cardPoints[left], cardPoints[right])

        return max(
            cardPoints[left] + self.max_score(cardPoints, k - 1, left+1, right),
            cardPoints[right] + self.max_score(cardPoints, k - 1, left, right-1)
        )


obj = Solution()
obj.display(3, [1, 2, 3, 4, 5, 6, 1])
obj.display(2, [2, 2, 2])
obj.display(7, [9, 7, 7, 9, 7, 7, 9])
obj.display(26, [30, 88, 33, 37, 18, 77, 54, 73, 31, 88, 93, 25, 18, 31, 71, 8, 97, 20, 98, 16, 65, 40, 18, 25, 13, 51, 59])

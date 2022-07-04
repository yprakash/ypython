# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/738083541/
    # O(1) only 2 lookups
    def candy(self, ratings):
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candies[i] = 1 + candies[i-1]

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = 1 + candies[i+1]
        return sum(candies)

    # https://leetcode.com/submissions/detail/738077217/
    # Recursion but still O(1)
    def candy2(self, ratings):
        candies = [0] * len(ratings)
        for i, r in enumerate(ratings):
            candies[i] = self.get_candies(i, ratings, candies)
        return sum(candies)

    def get_candies(self, index, ratings, candies):
        if candies[index] > 0:  # Its already assigned
            return candies[index]
        left, right = 0, 0

        if index > 0 and ratings[index-1] < ratings[index]:
            left = self.get_candies(index-1, ratings, candies)
        if index < len(ratings)-1 and ratings[index+1] < ratings[index]:
            right = self.get_candies(index+1, ratings, candies)
        candies[index] = 1 + max(left, right)
        return candies[index]


obj = Solution()
print(obj.candy([1, 0, 2]))  # 5 children get 2, 1, 2 candies respectively
print(obj.candy([1, 2, 2]))  # 4 children get 1, 2, 1 candies respectively
print(obj.candy([1, 2, 3, 2]))  # 7 - 1, 2, 3, 1 candies respectively

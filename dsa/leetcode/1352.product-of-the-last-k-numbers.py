# @author: yprakash
# https://leetcode.com/submissions/detail/826308553/

class ProductOfNumbers:
    def __init__(self):
        self.index = 0
        self.products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.index = 0
            self.products = []
        elif self.index == 0:
            self.index += 1
            self.products.append(num)
        else:
            self.index += 1
            self.products.append(num * self.products[-1])

    def getProduct(self, k: int) -> int:
        if k > self.index:
            return 0
        if k == self.index:
            return self.products[-1]
        return self.products[-1] // self.products[self.index - k - 1]

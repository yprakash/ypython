# @author: yprakash
from collections import deque


class StockSpanner:
    # https://leetcode.com/submissions/detail/826107546/
    def __init__(self):
        self.index = 0
        self.stack = deque()

    def next(self, price: int) -> int:
        # Always make sure the stack's elements are in decreasing order from '0' bottom
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        if self.stack:
            res = self.index - self.stack[-1][1]
        else:  # all elements in stream till now are <= today's price
            res = self.index + 1

        self.stack.append((price, self.index))
        self.index += 1
        return res


if __name__ == "__main__":
    testcases = [
        [10, 20, 15, 10, 18, 22],  # [1, 2, 1, 1, 3, 6]
        [100, 80, 60, 70, 60, 75, 85],  # [1, 1, 1, 2, 1, 4, 6]
        [28, 14, 28, 35, 46, 53, 66, 80, 87, 88],  # [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    for testcase in testcases:
        obj = StockSpanner()
        print([obj.next(p) for p in testcase])

# @author: yprakash

class Solution(object):
    def fib_yield(self, n):
        a, b = 0, 1

        while n > 1:
            n -= 1
            a, b = b, a + b
            yield a, b

    # https://leetcode.com/submissions/detail/739707829/
    # Using Generators and yield
    def fib(self, n):
        if n <= 1:
            return n
        func = self.fib_yield(n)

        while True:
            try:
                ans = next(func)
            except StopIteration:
                return ans[1]

    # https://leetcode.com/submissions/detail/739110272/
    def fib2(self, n):
        if n <= 1:
            return n
        a, b = 0, 1

        for i in range(1, n):
            a, b = b, a+b
        return b


obj = Solution()
for i in range(10):
    print(obj.fib(i))

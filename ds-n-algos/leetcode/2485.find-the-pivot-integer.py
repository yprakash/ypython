class Solution:
    # https://leetcode.com/contest/weekly-contest-321/submissions/detail/850401989/
    def pivotInteger(self, n: int) -> int:
        i = n
        total = (n * (n + 1)) // 2
        left, right = total, n

        while left > right:
            left -= i
            i -= 1
            right += i

        return i if left == right else -1

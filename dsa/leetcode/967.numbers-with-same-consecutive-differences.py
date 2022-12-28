# @author: yprakash
from collections import deque


class Solution(object):
    # https://leetcode.com/submissions/detail/790599828/
    def numsSameConsecDiff(self, n, k):
        res = set()
        q = deque()
        for i in range(1, 10):
            q.append(('', i))

        while q:
            num, d = q.popleft()
            num += str(d)
            if len(num) == n:
                res.add(int(num))
                continue

            if d + k < 10:
                q.append((num, d + k))
            if d - k >= 0:
                q.append((num, d - k))

        return res


if __name__ == "__main__":
    testcases = [
        [3, 7],  # [181,292,707,818,929]
        [2, 0],  # [11,22,33,44,55,66,77,88,99]
    ]
    obj = Solution()
    for n, k in testcases:
        print(obj.numsSameConsecDiff(n, k))

# @author: yprakash
from collections import deque


class Solution(object):
    # https://leetcode.com/submissions/detail/809768596/
    def pushDominoes(self, dominoes):
        dom = list(dominoes)
        q = deque()
        for i, d in enumerate(dominoes):
            if d != '.':  # make sure to append from Left to Right
                q.append((i, d))

        while q:
            i, d = q.popleft()
            if d == 'L':
                if i > 0 and dom[i-1] == '.':
                    # at this point dom[i-2] can never be 'R' bcoz of below logic
                    q.append((i-1, "L"))
                    dom[i-1] = "L"
            elif d == 'R':
                if i + 1 < len(dominoes) and dom[i + 1] == ".":
                    if i + 2 < len(dominoes) and dom[i + 2] == "L":
                        q.popleft()
                    else:
                        q.append((i + 1, "R"))
                        dom[i + 1] = "R"

        return ''.join(dom)


if __name__ == "__main__":
    testcases = [
        "RR.L",  # "RR.L"
        ".L.R...LR..L..",  # "LL.RR.LLRRLL.."
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.pushDominoes(testcase))

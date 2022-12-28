# @author: yprakash

class Solution(object):
    def can_replace(self, stamp, target, pos):
        for ch in stamp:
            if target[pos] != '?' and target[pos] != ch:
                return False
            pos += 1
        return True

    def replace(self, target, index, n, count):
        for i in range(index, index + n):
            if target[i] != '?':
                target[i] = '?'
                count += 1
        return count

    # https://leetcode.com/submissions/detail/779381241/
    def movesToStamp(self, stamp, target):
        res = []
        count = 0
        target = list(target)
        indices = range(1 + len(target) - len(stamp))
        visited = [False] * len(target)

        while count < len(target):
            changed = False
            for i in indices:
                if visited[i] or not self.can_replace(stamp, target, i):
                    continue

                count = self.replace(target, i, len(stamp), count)
                visited[i] = True
                changed = True
                res.append(i)
                if count == len(target):
                    break

            if not changed:
                return []

        res.reverse()
        return res  # res.reverse() returns None


if __name__ == "__main__":
    testcases = [
        ["abc", "ababc"],  # [0, 2] or [1, 0, 2]
        ["abca", "aabcaca"]  # [3, 0, 1]
    ]
    obj = Solution()
    for testcase in testcases:
        print(obj.movesToStamp(testcase[0], testcase[1]))

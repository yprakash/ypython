# @author: yprakash

class Solution(object):
    def total_time(self, index, inform_time, subordinates):
        if inform_time[index] == 0:  # same as if len(subordinates[index]) == 0
            return 0

        return inform_time[index] + max([
            self.total_time(subid, inform_time, subordinates) for subid in subordinates[index]
        ])

    # DFS: https://leetcode.com/submissions/detail/760735872/
    def numOfMinutes(self, n, headID, manager, informTime):
        subordinates = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                subordinates[m].append(i)
        print(subordinates)
        return self.total_time(headID, informTime, subordinates)


testcases = [
    [7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]]  # 21
]
obj = Solution()
for testcase in testcases:
    print(obj.numOfMinutes(testcase[0], testcase[1], testcase[2], testcase[3]))

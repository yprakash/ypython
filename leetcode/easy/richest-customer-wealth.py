class Solution:
    # https://leetcode.com/submissions/detail/706649627/
    def maximum(self, accounts: List[List[int]]) -> int:
        for ac in accounts:
            yield sum(ac)

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        gen = self.maximum(accounts)
        m = 0
        i = 0
        while i < len(accounts):
            i += 1
            n = next(gen)
            if m < n:
                m = n
        return m

    # https://leetcode.com/submissions/detail/706640091/
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max((sum(bal) for bal in accounts))

    # https://leetcode.com/submissions/detail/706400256/
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(bal) for bal in accounts)

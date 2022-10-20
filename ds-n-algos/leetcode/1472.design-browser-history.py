# @author: yprakash
# https://leetcode.com/submissions/detail/826716675/

class BrowserHistory:
    def __init__(self, homepage: str):
        self.end = 0
        self.curr = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr < len(self.history):
            self.history[self.curr] = url
        else:
            self.history.append(url)
        self.end = self.curr  # Invalidates forward history from pos self.end

    def back(self, steps: int) -> str:
        while steps and self.curr:
            steps -= 1
            self.curr -= 1
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        while steps and self.curr < self.end:
            steps -= 1
            self.curr += 1
        return self.history[self.curr]

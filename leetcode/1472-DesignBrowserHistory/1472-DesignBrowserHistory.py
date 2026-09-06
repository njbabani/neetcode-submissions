# Last updated: 9/6/2026, 2:55:43 PM
class BrowserHistory:

    def __init__(self, homepage: str):
        self.backward_stack = []
        self.forward_stack = []
        self.backward_stack.append(homepage)

    def visit(self, url: str) -> None:
        self.backward_stack.append(url)
        self.forward_stack = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.backward_stack) > 1:
            self.forward_stack.append(self.backward_stack[-1])
            self.backward_stack.pop()
            steps -= 1
        return self.backward_stack[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.backward_stack.append(self.forward_stack[-1])
            self.forward_stack.pop()
            steps -= 1
        return self.backward_stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
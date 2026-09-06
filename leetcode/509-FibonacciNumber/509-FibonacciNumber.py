# Last updated: 9/6/2026, 2:55:54 PM
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        f0, f1 = 0, 1

        for i in range(2, n + 1):
            fn = f0 + f1
            f1, f0 = fn, f1

        return fn
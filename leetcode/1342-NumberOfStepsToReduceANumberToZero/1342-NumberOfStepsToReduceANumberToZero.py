# Last updated: 9/6/2026, 2:55:47 PM
class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = 0
        while num != 0:
            if num % 2 == 0:
                num = num >> 1
            else:
                num -= 1
            n += 1
        return n
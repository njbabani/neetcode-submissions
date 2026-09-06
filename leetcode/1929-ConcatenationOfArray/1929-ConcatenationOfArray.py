# Last updated: 9/6/2026, 2:55:24 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for i in range(n):
            ans[i] = ans[i + n] = nums[i]

        return ans

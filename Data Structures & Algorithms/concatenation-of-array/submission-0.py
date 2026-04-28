class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        idx = 0
        for i in range(n):
            ans[i] = nums[i]
        for j in range(n, 2*n):
            ans[j] = nums[idx]
            idx += 1

        return ans
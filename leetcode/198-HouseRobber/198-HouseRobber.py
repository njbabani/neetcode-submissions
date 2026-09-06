# Last updated: 9/6/2026, 2:56:21 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        cache = [
            nums[0],
            max(nums[0], nums[1]),
            -1
        ]

        for i in range(2, n):
            cache[2] = max(cache[0] + nums[i], cache[1])
            cache[0], cache[1] = cache[1], cache[2]

        return cache[2]
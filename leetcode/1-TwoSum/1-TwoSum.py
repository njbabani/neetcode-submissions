# Last updated: 9/6/2026, 2:56:42 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map (one-pass)
        prev_map = {} # num -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev_map:
                return [prev_map[complement], i]
            else:
                prev_map[num] = i
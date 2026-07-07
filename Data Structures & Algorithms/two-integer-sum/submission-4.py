class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map (two-pass)
        map = {} # num -> index

        for i, num in enumerate(nums):
            map[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in map and map[complement] != i:
                return[i, map[complement]]

        return []
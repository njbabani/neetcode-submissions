class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Set length
        return len(set(nums)) != len(nums)
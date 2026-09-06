# Last updated: 9/6/2026, 2:56:18 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])

        return False
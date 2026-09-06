# Last updated: 9/6/2026, 2:56:30 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        
        return l
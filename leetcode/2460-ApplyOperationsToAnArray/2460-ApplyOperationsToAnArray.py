# Last updated: 9/6/2026, 2:55:12 PM
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            else:
                continue
        
        result = [nonzero for nonzero in nums if nonzero != 0] + [zero for zero in nums if zero == 0]

        return result
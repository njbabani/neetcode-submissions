# Last updated: 9/6/2026, 2:55:40 PM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j and nums[i] == nums[j]:
                    result += 1
        
        return result
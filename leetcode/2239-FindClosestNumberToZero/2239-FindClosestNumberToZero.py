# Last updated: 9/6/2026, 2:55:21 PM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Store the closest value
        close = nums[0]

        for num in nums:
            if abs(num) < abs(close) or (abs(num) == abs(close) and num > close):
                close = num
        
        return close
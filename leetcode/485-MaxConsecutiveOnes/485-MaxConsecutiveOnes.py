# Last updated: 9/6/2026, 2:56:01 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 0

        return max_cnt
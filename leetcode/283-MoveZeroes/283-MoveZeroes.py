# Last updated: 9/6/2026, 2:56:11 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0 # Keeps track of nonzero values
        fast = 0 # Iterates through array

        while fast < len(nums):
            if nums[fast] != 0:
                # Swap the numbers
                nums[slow], nums[fast] = nums[fast], nums[slow]

                # Since we swapped, we move the slow pointer
                slow += 1

            fast += 1
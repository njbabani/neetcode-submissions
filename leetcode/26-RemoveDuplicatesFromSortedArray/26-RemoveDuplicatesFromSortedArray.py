# Last updated: 9/6/2026, 2:56:31 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # To keep track of which index the unique num is at
        j = 1

        # Iterate through the array
        for i in range(1, len(nums)):
            # Next number is different from prior
            if nums[i] != nums[i - 1]:
                # Replace the next unique num with current num in array
                nums[j] = nums[i]

                # Move onto next num
                j += 1

        return j

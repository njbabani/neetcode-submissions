class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashmap of numbers that have appeared
        nums_hash = {}

        for i in range(len(nums)):
            if nums[i] in nums_hash:
                return True
            else:
                nums_hash[nums[i]] = 1
        
        return False
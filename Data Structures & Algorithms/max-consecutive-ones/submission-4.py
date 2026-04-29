class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        solution = 'iteration'

        if solution == 'brute':
            max_count = 0

            for i in range(len(nums)):
                # Second for loop starts at i so reset count
                count = 0
                for j in range(i, len(nums)):
                    if nums[j] == 0:
                        break
                    count += 1
                    max_count = max(max_count, count)

            return max_count
                

        if solution == 'iteration':
            count = max_count = 0

            for i in range(len(nums)):
                if nums[i] == 1:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    count = 0
            
            return max_count
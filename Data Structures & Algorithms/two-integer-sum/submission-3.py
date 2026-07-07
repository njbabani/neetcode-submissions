class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointers with sorting
        ans = []

        for i, num in enumerate(nums):
            ans.append([num, i])

        ans.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            curr = ans[l][0] + ans[r][0]
            if curr == target:
                small_index = min(ans[l][1], ans[r][1])
                big_index = max(ans[l][1], ans[r][1])
                return [small_index, big_index]
            elif curr < target:
                l += 1
            else:
                r -= 1

        return[]
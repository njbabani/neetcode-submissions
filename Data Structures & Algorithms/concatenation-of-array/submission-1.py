class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        solution = "1p"
        n = len(nums)
        # Iteration two pass
        if solution == "2p":
            ans = []
            for i in range(2):
                for j in range(n):
                    ans.append(nums[j])

        # Iteration one pass
        if solution == "1p":
            ans = [0] * (2 * n)
            for i in range(n):
                ans[i] = nums[i]
                ans[i + n] = nums[i]
        
        return ans
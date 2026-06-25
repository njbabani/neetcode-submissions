class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        suffix_max = [0] * n
        suffix_max[n - 1] = -1

        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(arr[i+1], suffix_max[i+1])

        return suffix_max
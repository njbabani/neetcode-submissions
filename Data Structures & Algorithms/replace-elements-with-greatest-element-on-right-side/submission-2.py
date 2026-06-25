class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            idx = i+1
            arr[i] = max(arr[idx:len(arr)])
        
        arr[-1] = -1

        return arr
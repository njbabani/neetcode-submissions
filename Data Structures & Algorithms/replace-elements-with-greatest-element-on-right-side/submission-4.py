class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_val = -1
            for j in range(i + 1, len(arr)):
                max_val = max(max_val, arr[j])
            
            arr[i] = max_val

        return arr
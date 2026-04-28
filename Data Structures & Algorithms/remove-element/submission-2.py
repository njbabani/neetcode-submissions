class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []

        for i in range(len(nums)):
            if val != nums[i]:
                temp.append(nums[i])

        for j in range(len(temp)):
            nums[j] = temp[j]

        return len(temp)
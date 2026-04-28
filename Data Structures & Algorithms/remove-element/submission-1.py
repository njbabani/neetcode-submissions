class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        solution = "tp"

        # Brute force
        if solution == "brute":
            temp = []

            for i in range(len(nums)):
                if nums[i] == val:
                    continue
                temp.append(nums[i])

            for i in range(len(temp)):
                nums[i] = temp[i]

            return len(temp)

        # Two pointers
        if solution == "tp":
            left = 0

            for right in range(len(nums)):
                if nums[right] != val:
                    nums[left] = nums[right]
                    left += 1

            return left

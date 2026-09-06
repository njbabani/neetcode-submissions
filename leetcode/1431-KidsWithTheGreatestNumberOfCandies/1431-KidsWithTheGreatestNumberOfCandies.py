# Last updated: 9/6/2026, 2:55:44 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum_candies = max(candies)

        output = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum_candies:
                output.append(True)
            else:
                output.append(False)

        return output

# Last updated: 9/6/2026, 2:56:26 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = int(999999)
        profit = int(-99999)

        for i in range(len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            if prices[i] - lowest_price > profit:
                profit = prices[i] - lowest_price
        
        return profit
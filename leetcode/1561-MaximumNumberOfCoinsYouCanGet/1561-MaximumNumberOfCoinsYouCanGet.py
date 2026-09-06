# Last updated: 9/6/2026, 2:55:35 PM
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        my_coins = int(0)

        n = len(piles)

        for i in range(n // 3, n, 2):
            my_coins += piles[i]

        return my_coins
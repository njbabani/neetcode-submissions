# Last updated: 9/6/2026, 2:55:33 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialise the maximum wealth value holder
        max_wealth = 0

        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            max_wealth = max(wealth, max_wealth)

        return max_wealth
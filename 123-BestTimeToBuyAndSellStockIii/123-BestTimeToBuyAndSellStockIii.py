# Last updated: 7/9/2026, 10:08:23 AM
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0] * n for _ in range(3)]

        for k in range(1, 3):  
            max_diff = -prices[0]
            for i in range(1, n):
                dp[k][i] = max(dp[k][i-1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[k-1][i] - prices[i])

        return dp[2][n-1]

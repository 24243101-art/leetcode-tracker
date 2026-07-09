# Last updated: 7/9/2026, 10:08:28 AM
class Solution:
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]  

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]

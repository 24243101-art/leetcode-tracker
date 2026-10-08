# Last updated: 10/8/2026, 10:23:53 AM
1class Solution:
2    def numSquares(self, n):
3        dp = [float('inf')] * (n + 1)
4
5        dp[0] = 0
6
7        for i in range(1, n + 1):
8            j = 1
9
10            while j * j <= i:
11                square = j * j
12
13                dp[i] = min(dp[i], dp[i - square] + 1)
14
15                j += 1
16
17        return dp[n]
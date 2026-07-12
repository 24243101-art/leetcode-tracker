# Last updated: 7/12/2026, 9:05:24 AM
1class Solution(object):
2    def maxConsistentColumns(self, grid, limit):
3        R = len(grid)
4        C = len(grid[0])
5        dp = [1] * C
6        for j in range(1, C):
7            for i in range(j):
8                if all(abs(grid[r][i] - grid[r][j]) <= limit for r in range(R)):
9                    dp[j] = max(dp[j], dp[i] + 1)
10        return max(dp)
11        
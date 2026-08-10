# Last updated: 8/10/2026, 9:08:12 PM
1class Solution:
2    def winnerSquareGame(self, n: int) -> bool:
3        dp = [False] * (n + 1)
4
5        for i in range(1, n + 1):
6            j = 1
7
8            while j * j <= i:
9                if not dp[i - j * j]:
10                    dp[i] = True
11                    break
12                j += 1
13
14        return dp[n]
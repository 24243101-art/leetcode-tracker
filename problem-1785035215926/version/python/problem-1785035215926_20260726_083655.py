# Last updated: 7/26/2026, 8:36:55 AM
1class Solution:
2    def countValidSequences(self, n: int, k: int) -> int:
3        MOD = 10 ** 9 + 7
4        if n < k:
5            return 0
6        def nCr(N, R):
7            if R < 0 or R > N: return 0
8            R = min(R, N - R)
9            num = den = 1
10            for i in range(R):
11                num = (num * (N - i)) % MOD
12                den = (den * (i + 1)) % MOD
13            return (num * pow(den, MOD - 2, MOD)) % MOD
14        total_ways = nCr(n - 1, k - 1)
15        odd_ways = 0
16        if (n - k) % 2 == 0:
17            m = (n - k) // 2
18            odd_ways = nCr(m + k - 1, k - 1)
19        ans = (total_ways - odd_ways + MOD) % MOD
20        return ans
21
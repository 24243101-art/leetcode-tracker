# Last updated: 8/21/2026, 9:17:46 PM
1class Solution:
2    def findKthSmallest(self, coins, k):
3
4        def gcd(a, b):
5            while b:
6                a, b = b, a % b
7            return a
8
9        def lcm(a, b):
10            return a // gcd(a, b) * b
11        coins.sort()
12        useful = []
13        for c in coins:
14            redundant = False
15
16            for x in useful:
17                if c % x == 0:
18                    redundant = True
19                    break
20
21            if not redundant:
22                useful.append(c)
23
24        coins = useful
25
26        def count(x):
27            total = 0
28            n = len(coins)
29            for mask in range(1, 1 << n):
30                multiple = 1
31                bits = 0
32
33                for i in range(n):
34                    if mask & (1 << i):
35                        bits += 1
36                        multiple = lcm(multiple, coins[i])
37
38                        if multiple > x:
39                            break
40
41                else:
42                    if bits % 2 == 1:
43                        total += x // multiple
44                    else:
45                        total -= x // multiple
46
47            return total
48        left = 1
49        right = min(coins) * k
50
51        while left < right:
52            mid = (left + right) // 2
53
54            if count(mid) >= k:
55                right = mid
56            else:
57                left = mid + 1
58
59        return left
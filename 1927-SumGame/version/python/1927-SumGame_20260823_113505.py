# Last updated: 8/23/2026, 11:35:05 AM
1class Solution:
2    def sumGame(self, num: str) -> bool:
3        n = len(num)
4        half = n // 2
5        left_sum = 0
6        right_sum = 0
7        left_q = 0
8        right_q = 0
9        for i in range(half):
10            if num[i] == '?':
11                left_q += 1
12            else:
13                left_sum += int(num[i])
14        for i in range(half, n):
15            if num[i] == '?':
16                right_q += 1
17            else:
18                right_sum += int(num[i])
19        diff = left_sum - right_sum
20        if left_q == right_q:
21            return diff != 0
22        if left_q > right_q:
23            return diff + (left_q - right_q) * 4.5 != 0
24        else:
25            return diff - (right_q - left_q) * 4.5 != 0
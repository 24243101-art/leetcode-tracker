# Last updated: 8/28/2026, 9:41:40 AM
1class Solution:
2    def nthUglyNumber(self, n):
3        ugly = [1] * n
4
5        i2 = 0
6        i3 = 0
7        i5 = 0
8
9        for i in range(1, n):
10            next2 = ugly[i2] * 2
11            next3 = ugly[i3] * 3
12            next5 = ugly[i5] * 5
13
14            ugly[i] = min(next2, next3, next5)
15
16            if ugly[i] == next2:
17                i2 += 1
18
19            if ugly[i] == next3:
20                i3 += 1
21
22            if ugly[i] == next5:
23                i5 += 1
24
25        return ugly[n - 1]
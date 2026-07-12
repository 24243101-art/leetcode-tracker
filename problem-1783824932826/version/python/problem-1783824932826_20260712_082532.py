# Last updated: 7/12/2026, 8:25:32 AM
1import math
2class Solution(object):
3    def minimumCost(self, nums, k):
4        res, cost, ops = k, 0, 0
5        for x in nums:
6            if res < x:
7                n =  (x - res + k - 1) // k
8                cost += n * ops + n * (n + 1) // 2
9                ops += n
10                res += n * k
11            res -= x
12        return cost % (10**9 + 7)
13        
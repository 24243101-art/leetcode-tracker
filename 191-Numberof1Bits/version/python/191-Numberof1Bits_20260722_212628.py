# Last updated: 7/22/2026, 9:26:28 PM
1class Solution:
2    def hammingWeight(self, n):
3        count = 0
4
5        while n:
6            count += 1
7            n &= (n - 1)
8
9        return count
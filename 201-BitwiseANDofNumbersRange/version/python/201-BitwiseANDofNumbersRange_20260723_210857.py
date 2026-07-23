# Last updated: 7/23/2026, 9:08:57 PM
1class Solution(object):
2    def rangeBitwiseAnd(self, left, right):
3        shift = 0
4
5        while left < right:
6            left >>= 1
7            right >>= 1
8            shift += 1
9
10        return left << shift
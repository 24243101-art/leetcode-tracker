# Last updated: 7/22/2026, 9:22:42 PM
1class Solution:
2    def reverseBits(self, n):
3        result = 0
4
5        for i in range(32):
6            result = (result << 1) | (n & 1)
7            n >>= 1
8
9        return result
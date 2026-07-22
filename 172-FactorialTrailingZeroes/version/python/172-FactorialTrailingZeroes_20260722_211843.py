# Last updated: 7/22/2026, 9:18:43 PM
1class Solution:
2    def trailingZeroes(self, n):
3        count = 0
4
5        while n > 0:
6            n //= 5
7            count += n
8
9        return count
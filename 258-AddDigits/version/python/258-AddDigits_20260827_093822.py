# Last updated: 8/27/2026, 9:38:22 AM
1class Solution:
2    def addDigits(self, num: int) -> int:
3        while num >= 10:
4            total = 0
5
6            while num > 0:
7                total += num % 10
8                num //= 10
9
10            num = total
11
12        return num
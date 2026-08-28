# Last updated: 8/28/2026, 9:38:52 AM
1class Solution:
2    def isUgly(self, n):
3        if n <= 0:
4            return False
5
6        while n % 2 == 0:
7            n //= 2
8
9        while n % 3 == 0:
10            n //= 3
11
12        while n % 5 == 0:
13            n //= 5
14
15        return n == 1
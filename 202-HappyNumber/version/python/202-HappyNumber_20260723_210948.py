# Last updated: 7/23/2026, 9:09:48 PM
1class Solution(object):
2    def isHappy(self, n):
3        seen = set()
4
5        while n != 1 and n not in seen:
6            seen.add(n)
7            total = 0
8
9            while n > 0:
10                digit = n % 10
11                total += digit * digit
12                n //= 10
13
14            n = total
15
16        return n == 1
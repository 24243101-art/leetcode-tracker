# Last updated: 7/27/2026, 3:13:13 PM
1class Solution:
2    def countDigitOne(self, n):
3        count = 0
4        place = 1
5
6        while place <= n:
7            higher = n // (place * 10)
8            current = (n // place) % 10
9            lower = n % place
10
11            if current == 0:
12                count += higher * place
13            elif current == 1:
14                count += higher * place + lower + 1
15            else:
16                count += (higher + 1) * place
17
18            place *= 10
19
20        return count
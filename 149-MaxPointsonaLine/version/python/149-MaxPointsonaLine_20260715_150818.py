# Last updated: 7/15/2026, 3:08:18 PM
1from collections import defaultdict
2
3class Solution:
4    def gcd(self, a, b):
5        while b:
6            a, b = b, a % b
7        return abs(a)
8
9    def maxPoints(self, points):
10        n = len(points)
11
12        if n <= 2:
13            return n
14
15        ans = 0
16
17        for i in range(n):
18            slopes = defaultdict(int)
19
20            for j in range(i + 1, n):
21                dx = points[j][0] - points[i][0]
22                dy = points[j][1] - points[i][1]
23
24                g = self.gcd(dx, dy)
25                dx //= g
26                dy //= g
27
28                if dx < 0:
29                    dx = -dx
30                    dy = -dy
31                elif dx == 0:
32                    dy = 1
33                elif dy == 0:
34                    dx = 1
35
36                slopes[(dx, dy)] += 1
37
38            if slopes:
39                ans = max(ans, max(slopes.values()) + 1)
40            else:
41                ans = max(ans, 1)
42
43        return ans
# Last updated: 8/23/2026, 5:09:57 PM
1class Solution:
2    def diffWaysToCompute(self, expression):
3        def solve(s):
4            result = []
5
6            for i in range(len(s)):
7                if s[i] in "+-*":
8                    left = solve(s[:i])
9                    right = solve(s[i + 1:])
10
11                    for a in left:
12                        for b in right:
13                            if s[i] == "+":
14                                result.append(a + b)
15                            elif s[i] == "-":
16                                result.append(a - b)
17                            else:
18                                result.append(a * b)
19
20            if not result:
21                result.append(int(s))
22
23            return result
24
25        return solve(expression)
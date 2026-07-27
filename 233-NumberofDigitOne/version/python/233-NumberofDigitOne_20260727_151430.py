# Last updated: 7/27/2026, 3:14:30 PM
1class Solution:
2    def diffWaysToCompute(self, expression):
3
4        memo = {}
5
6        def solve(exp):
7
8            if exp in memo:
9                return memo[exp]
10
11            result = []
12
13            for i in range(len(exp)):
14
15                if exp[i] in "+-*":
16
17                    left = solve(exp[:i])
18                    right = solve(exp[i + 1:])
19
20                    for l in left:
21                        for r in right:
22
23                            if exp[i] == "+":
24                                result.append(l + r)
25
26                            elif exp[i] == "-":
27                                result.append(l - r)
28
29                            else:
30                                result.append(l * r)
31
32            if not result:
33                result.append(int(exp))
34
35            memo[exp] = result
36            return result
37
38        return solve(expression)
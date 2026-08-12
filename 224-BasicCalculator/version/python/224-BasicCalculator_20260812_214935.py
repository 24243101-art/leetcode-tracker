# Last updated: 8/12/2026, 9:49:35 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        result = 0
5        number = 0
6        sign = 1
7
8        for ch in s:
9            if ch.isdigit():
10                number = number * 10 + int(ch)
11
12            elif ch == '+':
13                result += sign * number
14                number = 0
15                sign = 1
16
17            elif ch == '-':
18                result += sign * number
19                number = 0
20                sign = -1
21
22            elif ch == '(':
23                stack.append(result)
24                stack.append(sign)
25
26                result = 0
27                sign = 1
28
29            elif ch == ')':
30                result += sign * number
31                number = 0
32
33                sign = stack.pop()
34
35                previous_result = stack.pop()
36
37                result = previous_result + sign * result
38
39        result += sign * number
40
41        return result
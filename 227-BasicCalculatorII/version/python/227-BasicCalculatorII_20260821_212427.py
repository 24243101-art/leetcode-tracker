# Last updated: 8/21/2026, 9:24:27 PM
1class Solution:
2    def calculate(self, s):
3        stack = []
4        num = 0
5        sign = '+'
6
7        for i in range(len(s)):
8            ch = s[i]
9
10            if ch.isdigit():
11                num = num * 10 + int(ch)
12
13            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
14
15                if sign == '+':
16                    stack.append(num)
17
18                elif sign == '-':
19                    stack.append(-num)
20
21                elif sign == '*':
22                    stack.append(stack.pop() * num)
23
24                elif sign == '/':
25                    prev = stack.pop()
26
27                    # Truncate toward zero without using float
28                    if prev < 0:
29                        stack.append(-((-prev) // num))
30                    else:
31                        stack.append(prev // num)
32
33                sign = ch
34                num = 0
35
36        return sum(stack)
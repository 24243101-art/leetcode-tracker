# Last updated: 10/7/2026, 9:01:39 AM
1from collections import deque
2
3class Solution:
4    def removeInvalidParentheses(self, s):
5        def is_valid(string):
6            balance = 0
7
8            for ch in string:
9                if ch == '(':
10                    balance += 1
11
12                elif ch == ')':
13                    balance -= 1
14
15                    if balance < 0:
16                        return False
17
18            return balance == 0
19
20        queue = deque([s])
21        visited = {s}
22        result = []
23
24        while queue:
25
26            for _ in range(len(queue)):
27                current = queue.popleft()
28
29                if is_valid(current):
30                    result.append(current)
31                    continue
32
33                for i in range(len(current)):
34
35                    if current[i] not in '()':
36                        continue
37
38                    new_string = current[:i] + current[i + 1:]
39
40                    if new_string not in visited:
41                        visited.add(new_string)
42                        queue.append(new_string)
43
44            if result:
45                return result
46
47        return [""]
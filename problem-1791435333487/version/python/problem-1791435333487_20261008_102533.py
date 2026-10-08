# Last updated: 10/8/2026, 10:25:33 AM
1class Solution:
2    def addOperators(self, num, target):
3        result = []
4
5        def backtrack(index, expression, current, prev):
6            if index == len(num):
7                if current == target:
8                    result.append(expression)
9                return
10
11            for end in range(index, len(num)):
12                
13                if end > index and num[index] == '0':
14                    break
15
16                number = int(num[index:end + 1])
17
18                if index == 0:
19                    backtrack(
20                        end + 1,
21                        str(number),
22                        number,
23                        number
24                    )
25
26                else:
27                    backtrack(
28                        end + 1,
29                        expression + "+" + str(number),
30                        current + number,
31                        number
32                    )
33
34                    backtrack(
35                        end + 1,
36                        expression + "-" + str(number),
37                        current - number,
38                        -number
39                    )
40
41                    backtrack(
42                        end + 1,
43                        expression + "*" + str(number),
44                        current - prev + prev * number,
45                        prev * number
46                    )
47
48        backtrack(0, "", 0, 0)
49
50        return result
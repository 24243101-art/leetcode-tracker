# Last updated: 9/11/2026, 10:08:45 AM
1class Solution:
2    def totalNumbers(self, digits):
3        ans = set()
4
5        for i in range(len(digits)):
6            for j in range(len(digits)):
7                for k in range(len(digits)):
8                    if i == j or j == k or i == k:
9                        continue
10
11                    if digits[i] == 0:
12                        continue
13
14                    if digits[k] % 2 != 0:
15                        continue
16
17                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
18                    ans.add(num)
19
20        return len(ans)
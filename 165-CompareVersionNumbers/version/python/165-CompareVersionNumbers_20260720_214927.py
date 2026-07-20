# Last updated: 7/20/2026, 9:49:27 PM
1class Solution:
2    def compareVersion(self, version1, version2):
3        v1 = version1.split(".")
4        v2 = version2.split(".")
5
6        n = max(len(v1), len(v2))
7
8        for i in range(n):
9            num1 = int(v1[i]) if i < len(v1) else 0
10            num2 = int(v2[i]) if i < len(v2) else 0
11
12            if num1 < num2:
13                return -1
14            elif num1 > num2:
15                return 1
16
17        return 0
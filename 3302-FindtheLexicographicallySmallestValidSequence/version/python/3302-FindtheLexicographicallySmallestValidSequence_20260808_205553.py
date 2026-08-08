# Last updated: 8/8/2026, 8:55:53 PM
1class Solution:
2    def validSequence(self, word1: str, word2: str):
3        n = len(word1)
4        m = len(word2)
5
6        dp = [0] * (n + 1)
7        j = m - 1
8
9        for i in range(n - 1, -1, -1):
10            dp[i] = dp[i + 1]
11
12            if j >= 0 and word1[i] == word2[j]:
13                dp[i] += 1
14                j -= 1
15
16        last = [-1] * m
17
18        i = n - 1
19        j = m - 1
20
21        while i >= 0 and j >= 0:
22            if word1[i] == word2[j]:
23                last[j] = i
24                j -= 1
25            i -= 1
26
27        ans = []
28        i = 0
29        j = 0
30        canSkip = True
31
32        while i < n and j < m:
33            if word1[i] == word2[j]:
34                ans.append(i)
35                j += 1
36            elif canSkip and (j == m - 1 or i < last[j + 1]):
37                ans.append(i)
38                j += 1
39                canSkip = False
40            i += 1
41
42        if j < m:
43            return []
44
45        return ans
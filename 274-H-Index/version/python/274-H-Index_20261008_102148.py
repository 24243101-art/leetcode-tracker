# Last updated: 10/8/2026, 10:21:48 AM
1class Solution:
2    def hIndex(self, citations):
3        citations.sort(reverse=True)
4
5        h = 0
6
7        for i in range(len(citations)):
8            if citations[i] >= i + 1:
9                h = i + 1
10            else:
11                break
12
13        return h
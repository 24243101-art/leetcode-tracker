# Last updated: 7/26/2026, 8:24:21 AM
1class Solution:
2    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
3        timestamps = sorted(list(set([item[0] for item in series1] + [item[0] for item in series2])))
4        result = []
5        i, j = 0, 0
6        n1, n2 = len(series1), len(series2)
7        for t in timestamps:
8            while i < n1 and series1[i][0] < t:
9                i += 1
10            while j < n2 and series2[j][0] < t:
11                j += 1
12            val1 = series1[i][1] if i < n1 else 0
13            val2 = series2[j][1] if j < n2 else 0
14            result.append([t, val1 + val2])
15        return result
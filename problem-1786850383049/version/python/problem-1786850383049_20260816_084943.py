# Last updated: 8/16/2026, 8:49:43 AM
1class Solution:
2    def maximumGap(self, skill: str, station: str) -> int:
3        n = len(skill)
4        m = len(station)
5        if n == 1:
6            return 0
7        def is_compatible(worker_skill: str, station_capacity: str) -> bool:
8            return worker_skill in station_capacity or worker_skill == station_capacity
9        min_idx = [-1] * n
10        curr_station = 0
11        for i in range(n):
12            while curr_station < m and not is_compatible(skill[i], station[curr_station]):
13                curr_station += 1
14            if curr_station >= m:
15                return - 1
16            min_idx[i] = curr_station
17            curr_station += 1
18        max_idx = [-1] * n
19        curr_station = m - 1
20        for i in range(n - 1, -1, -1):
21            while curr_station >= 0 and not is_compatible(skill[i], station[curr_station]):
22                curr_station -= 1
23            if curr_station < 0:
24                return -1
25            max_idx[i] = curr_station
26            curr_station -= 1
27        max_gap = 0
28        for i in range(n - 1):
29            current_gap = max_idx[i + 1] - min_idx[i]
30            if current_gap > max_gap:
31                max_gap = current_gap
32        return max_gap
# Last updated: 8/16/2026, 8:38:17 AM
1class Solution:
2    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
3        max_light = max(lights)
4        arrivals = [t % period for t in arrivalTime]
5        low = 0
6        high = period
7        ans  = period
8        def check(W: int) -> bool:
9            for t in arrivals:
10                if not (t < max_light or t >= period - W):
11                    return False
12            return True
13        while low <= high:
14            mid = (low + high) // 2
15            if check(mid):
16                ans = mid
17                high = mid - 1
18            else:
19                low  = mid + 1
20        return ans
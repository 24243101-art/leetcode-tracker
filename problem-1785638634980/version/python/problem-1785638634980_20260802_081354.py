# Last updated: 8/2/2026, 8:13:54 AM
1class Solution:
2    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
3        arr = [b if x % 2 == 0 else -a for x in nums]
4        total = 0
5        pref = 0
6        sl = SortedList()
7        last_odd_idx = -1
8        p_sums = [0]
9        added_until = 0
10        for j, val in enumerate(arr):
11            pref += val
12            p_sums.append(pref)
13            if val == -a:
14                last_odd_idx = j
15            while added_until <= last_odd_idx:
16                sl.add(p_sums[added_until])
17                added_until += 1
18            if last_odd_idx != -1:
19                total += len(sl) - sl.bisect_left(pref)
20        return total
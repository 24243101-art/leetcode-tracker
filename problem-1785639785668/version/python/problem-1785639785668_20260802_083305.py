# Last updated: 8/2/2026, 8:33:05 AM
1import itertools
2import bisect
3class Solution:
4    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
5        n = len(tasks)
6        pref = [0] + list(itertools.accumulate(tasks))
7        total_cycle_time = pref[-1]
8        ans = []
9        curr_pos = 0
10        for time in shifts:
11            target_pos = curr_pos + time
12            if target_pos >= total_cycle_time:
13                ans.append(0)
14                curr_pos = 0
15            else:
16                completed_tasks = bisect.bisect_right(pref, target_pos) - 1
17                ans.append(n - completed_tasks)
18                curr_pos = target_pos
19        return ans
20        
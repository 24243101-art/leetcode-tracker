# Last updated: 7/28/2026, 7:14:27 PM
1from sortedcontainers import SortedList
2
3class Solution:
4    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
5        window = SortedList()
6
7        for i in range(len(nums)):
8            pos = window.bisect_left(nums[i] - valueDiff)
9
10            if pos < len(window) and abs(window[pos] - nums[i]) <= valueDiff:
11                return True
12
13            window.add(nums[i])
14
15            if len(window) > indexDiff:
16                window.remove(nums[i - indexDiff])
17
18        return False
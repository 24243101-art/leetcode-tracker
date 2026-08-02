# Last updated: 8/2/2026, 8:49:43 AM
1class Solution:
2    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
3        v = [0]
4        even, odd = 0 ,0
5        for num in nums:
6            if num % 2 == 0 : even += 1
7            else: odd += 1
8            v.append(b * even - a * odd)
9        valid_vals = []
10        total_valid = 0
11        last_added = 0
12        even, odd = 0, 0
13        for i, num in enumerate(nums):
14            if num % 2 != 0:
15                odd += 1
16                while last_added <= i:
17                    bisect.insort(valid_vals, v[last_added])
18                    last_added += 1
19            else:
20                even += 1
21            curr_v = b * even - a * odd
22            idx = bisect.bisect_left(valid_vals, curr_v)
23            total_valid += len(valid_vals) - idx
24        return total_valid
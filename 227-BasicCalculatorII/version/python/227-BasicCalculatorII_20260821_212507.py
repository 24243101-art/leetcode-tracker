# Last updated: 8/21/2026, 9:25:07 PM
1class Solution:
2    def summaryRanges(self, nums):
3        result = []
4
5        if not nums:
6            return result
7
8        start = nums[0]
9
10        for i in range(1, len(nums)):
11            if nums[i] != nums[i - 1] + 1:
12                if start == nums[i - 1]:
13                    result.append(str(start))
14                else:
15                    result.append(str(start) + "->" + str(nums[i - 1]))
16
17                start = nums[i]
18
19        if start == nums[-1]:
20            result.append(str(start))
21        else:
22            result.append(str(start) + "->" + str(nums[-1]))
23
24        return result
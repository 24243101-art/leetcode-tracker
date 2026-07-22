# Last updated: 7/22/2026, 9:16:31 PM
1class Solution:
2    def majorityElement(self, nums):
3        count = 0
4        candidate = None
5
6        for num in nums:
7            if count == 0:
8                candidate = num
9
10            if num == candidate:
11                count += 1
12            else:
13                count -= 1
14
15        return candidate
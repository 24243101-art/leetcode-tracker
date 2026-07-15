# Last updated: 7/15/2026, 3:16:42 PM
1class Solution:
2    def maxProduct(self, nums):
3        max_prod = nums[0]
4        min_prod = nums[0]
5        ans = nums[0]
6
7        for i in range(1, len(nums)):
8            if nums[i] < 0:
9                max_prod, min_prod = min_prod, max_prod
10
11            max_prod = max(nums[i], max_prod * nums[i])
12            min_prod = min(nums[i], min_prod * nums[i])
13
14            ans = max(ans, max_prod)
15
16        return ans
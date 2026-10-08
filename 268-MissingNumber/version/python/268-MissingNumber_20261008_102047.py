# Last updated: 10/8/2026, 10:20:47 AM
1class Solution:
2    def missingNumber(self, nums):
3        n = len(nums)
4        return n * (n + 1) // 2 - sum(nums)
5        
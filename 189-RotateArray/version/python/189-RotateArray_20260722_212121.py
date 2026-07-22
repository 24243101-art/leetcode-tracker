# Last updated: 7/22/2026, 9:21:21 PM
1class Solution:
2    def rotate(self, nums, k):
3        n = len(nums)
4        k %= n
5
6        nums.reverse()
7        nums[:k] = reversed(nums[:k])
8        nums[k:] = reversed(nums[k:])
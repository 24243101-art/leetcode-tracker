# Last updated: 10/8/2026, 10:26:21 AM
1class Solution:
2    def moveZeroes(self, nums):
3        insert = 0
4
5        for i in range(len(nums)):
6            if nums[i] != 0:
7                nums[insert], nums[i] = nums[i], nums[insert]
8                insert += 1
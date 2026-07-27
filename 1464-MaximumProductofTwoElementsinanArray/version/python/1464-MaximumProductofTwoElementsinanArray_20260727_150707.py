# Last updated: 7/27/2026, 3:07:07 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        a = max(nums)
4        nums.remove(a)
5        b = max(nums)
6        return (b - 1) * (a - 1)
7
8
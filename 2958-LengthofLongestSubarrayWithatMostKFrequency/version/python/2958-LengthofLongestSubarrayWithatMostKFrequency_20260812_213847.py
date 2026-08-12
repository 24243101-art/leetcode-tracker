# Last updated: 8/12/2026, 9:38:47 PM
1class Solution:
2    def maxSubarrayLength(self, nums, k):
3        left = 0
4        max_length = 0
5        freq = {}
6
7        for right in range(len(nums)):
8            freq[nums[right]] = freq.get(nums[right], 0) + 1
9
10            while freq[nums[right]] > k:
11                freq[nums[left]] -= 1
12                left += 1
13
14            max_length = max(max_length, right - left + 1)
15
16        return max_length
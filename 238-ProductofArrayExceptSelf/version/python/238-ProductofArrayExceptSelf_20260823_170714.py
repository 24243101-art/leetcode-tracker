# Last updated: 8/23/2026, 5:07:14 PM
1from collections import deque
2
3class Solution:
4    def maxSlidingWindow(self, nums, k):
5        dq = deque()
6        result = []
7
8        for i in range(len(nums)):
9            while dq and dq[0] <= i - k:
10                dq.popleft()
11            while dq and nums[dq[-1]] <= nums[i]:
12                dq.pop()
13            dq.append(i)
14            if i >= k - 1:
15                result.append(nums[dq[0]])
16
17        return result
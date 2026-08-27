# Last updated: 8/27/2026, 9:28:32 AM
1class Solution:
2    def productExceptSelf(self, nums):
3        n = len(nums)
4        answer = [1] * n
5
6        prefix = 1
7
8        for i in range(n):
9            answer[i] = prefix
10            prefix *= nums[i]
11
12        suffix = 1
13
14        for i in range(n - 1, -1, -1):
15            answer[i] *= suffix
16            suffix *= nums[i]
17
18        return answer
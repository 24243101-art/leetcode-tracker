# Last updated: 8/27/2026, 9:39:37 AM
1class Solution:
2    def singleNumber(self, nums):
3        xor = 0
4        for num in nums:
5            xor ^= num
6        diff = xor & -xor
7        a = 0
8        b = 0
9        for num in nums:
10            if num & diff:
11                a ^= num
12            else:
13                b ^= num
14        return [a, b]
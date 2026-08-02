# Last updated: 8/2/2026, 8:14:10 AM
1class Solution:
2    def maxPairStrength(self, nums: list[int]) -> int:
3        max_strength = 0
4        n = len(nums)
5        for i in range(n):
6            for j in range(i + 1, n):
7                a, b = nums[i], nums[j]
8                g = math.gcd(a, b)
9                current_strength = (a * b) // (g * g)
10                if current_strength > max_strength:
11                    max_strength = current_strength
12        return max_strength
# Last updated: 7/22/2026, 9:14:44 PM
1class Solution:
2    def twoSum(self, numbers, target):
3        left = 0
4        right = len(numbers) - 1
5
6        while left < right:
7            s = numbers[left] + numbers[right]
8
9            if s == target:
10                return [left + 1, right + 1]
11            elif s < target:
12                left += 1
13            else:
14                right -= 1
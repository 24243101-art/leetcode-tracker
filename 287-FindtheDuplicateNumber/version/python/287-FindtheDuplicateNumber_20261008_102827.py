# Last updated: 10/8/2026, 10:28:27 AM
1class Solution:
2    def findDuplicate(self, nums):
3        slow = nums[0]
4        fast = nums[0]
5
6        while True:
7            slow = nums[slow]
8            fast = nums[nums[fast]]
9
10            if slow == fast:
11                break
12
13        slow = nums[0]
14
15        while slow != fast:
16            slow = nums[slow]
17            fast = nums[fast]
18
19        return slow
# Last updated: 8/23/2026, 12:05:00 PM
1class Solution:
2    def majorityElement(self, nums):
3        candidate1 = None
4        candidate2 = None
5        count1 = 0
6        count2 = 0
7
8        for num in nums:
9
10            if num == candidate1:
11                count1 += 1
12
13            elif num == candidate2:
14                count2 += 1
15
16            elif count1 == 0:
17                candidate1 = num
18                count1 = 1
19
20            elif count2 == 0:
21                candidate2 = num
22                count2 = 1
23
24            else:
25                count1 -= 1
26                count2 -= 1
27
28        count1 = 0
29        count2 = 0
30
31        for num in nums:
32            if num == candidate1:
33                count1 += 1
34            elif num == candidate2:
35                count2 += 1
36
37        result = []
38        n = len(nums)
39
40        if count1 > n // 3:
41            result.append(candidate1)
42
43        if count2 > n // 3:
44            result.append(candidate2)
45
46        return result
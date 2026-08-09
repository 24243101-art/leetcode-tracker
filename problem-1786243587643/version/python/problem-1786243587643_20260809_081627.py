# Last updated: 8/9/2026, 8:16:27 AM
1class Solution:
2    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
3        from collections import defaultdict
4        n = len(parent)
5        adj = defaultdict(list)
6        for child in range(1, n):
7            adj[parent[child]].append(child)
8        depths = [0] * n
9        max_height = 0
10        stack = [(0,1)]
11        while stack:
12            curr, d = stack.pop()
13            depths[curr] = d
14            if d > max_height:
15                max_height = d
16            for child in adj[curr]:
17                stack.append((child, d + 1))
18        total_weight = 0
19        for i in range(n):
20            d = depths[i]
21            weight = nums[i] * (max_height - d + 1)
22            total_weight+= weight
23        return total_weight
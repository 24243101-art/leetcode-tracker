# Last updated: 7/23/2026, 8:46:26 PM
1class Solution:
2    def numIslands(self, grid):
3        if not grid:
4            return 0
5
6        rows = len(grid)
7        cols = len(grid[0])
8        islands = 0
9
10        def dfs(r, c):
11            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
12                return
13
14            grid[r][c] = "0"
15
16            dfs(r + 1, c)
17            dfs(r - 1, c)
18            dfs(r, c + 1)
19            dfs(r, c - 1)
20
21        for r in range(rows):
22            for c in range(cols):
23                if grid[r][c] == "1":
24                    islands += 1
25                    dfs(r, c)
26
27        return islands
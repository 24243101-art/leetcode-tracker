# Last updated: 8/23/2026, 5:08:32 PM
1class Solution:
2    def searchMatrix(self, matrix, target):
3        rows = len(matrix)
4        cols = len(matrix[0])
5
6        row = 0
7        col = cols - 1
8
9        while row < rows and col >= 0:
10            current = matrix[row][col]
11
12            if current == target:
13                return True
14
15            elif current > target:
16                col -= 1
17
18            else:
19                row += 1
20
21        return False
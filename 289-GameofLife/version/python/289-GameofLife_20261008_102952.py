# Last updated: 10/8/2026, 10:29:52 AM
1class Solution:
2    def gameOfLife(self, board):
3        m = len(board)
4        n = len(board[0])
5
6        directions = [
7            (-1, -1), (-1, 0), (-1, 1),
8            (0, -1),           (0, 1),
9            (1, -1),  (1, 0),  (1, 1)
10        ]
11
12        for i in range(m):
13            for j in range(n):
14
15                live = 0
16
17                for di, dj in directions:
18                    ni = i + di
19                    nj = j + dj
20
21                    if 0 <= ni < m and 0 <= nj < n:
22                        if board[ni][nj] == 1 or board[ni][nj] == 2:
23                            live += 1
24
25                if board[i][j] == 1:
26                    if live < 2 or live > 3:
27                        board[i][j] = 2
28
29                else:
30                    if live == 3:
31                        board[i][j] = 3
32
33        for i in range(m):
34            for j in range(n):
35                if board[i][j] == 2:
36                    board[i][j] = 0
37                elif board[i][j] == 3:
38                    board[i][j] = 1
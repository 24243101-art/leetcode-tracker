# Last updated: 7/27/2026, 10:20:30 AM
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.word = None
5
6
7class Solution:
8    def findWords(self, board, words):
9        root = TrieNode()
10
11        for word in words:
12            node = root
13            for ch in word:
14                if ch not in node.children:
15                    node.children[ch] = TrieNode()
16                node = node.children[ch]
17            node.word = word
18
19        rows = len(board)
20        cols = len(board[0])
21        result = []
22
23        def dfs(r, c, node):
24            ch = board[r][c]
25
26            if ch not in node.children:
27                return
28
29            nextNode = node.children[ch]
30
31            if nextNode.word:
32                result.append(nextNode.word)
33                nextNode.word = None     
34
35            board[r][c] = "#"
36
37            directions = [(1,0), (-1,0), (0,1), (0,-1)]
38
39            for dr, dc in directions:
40                nr = r + dr
41                nc = c + dc
42
43                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
44                    dfs(nr, nc, nextNode)
45
46            board[r][c] = ch
47
48        for i in range(rows):
49            for j in range(cols):
50                dfs(i, j, root)
51
52        return result
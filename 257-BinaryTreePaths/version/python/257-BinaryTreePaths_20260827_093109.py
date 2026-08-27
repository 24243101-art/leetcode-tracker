# Last updated: 8/27/2026, 9:31:09 AM
1class Solution:
2    def binaryTreePaths(self, root):
3        result = []
4
5        def dfs(node, path):
6            if not node:
7                return
8
9            path.append(str(node.val))
10
11            if not node.left and not node.right:
12                result.append("->".join(path))
13            else:
14                dfs(node.left, path)
15                dfs(node.right, path)
16            path.pop()
17
18        dfs(root, [])
19
20        return result
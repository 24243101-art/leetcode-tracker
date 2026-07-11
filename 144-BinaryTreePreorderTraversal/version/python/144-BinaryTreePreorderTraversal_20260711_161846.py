# Last updated: 7/11/2026, 4:18:46 PM
1class Solution:
2    def preorderTraversal(self, root):
3        result = []
4
5        def preorder(node):
6            if not node:
7                return
8            result.append(node.val)
9            preorder(node.left)
10            preorder(node.right)
11
12        preorder(root)
13        return result
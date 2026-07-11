# Last updated: 7/11/2026, 4:23:49 PM
1class Solution:
2    def postorderTraversal(self, root):
3        result = []
4
5        def postorder(node):
6            if not node:
7                return
8            postorder(node.left)
9            postorder(node.right)
10            result.append(node.val)
11
12        postorder(root)
13        return result
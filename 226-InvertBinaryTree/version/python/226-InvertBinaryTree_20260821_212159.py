# Last updated: 8/21/2026, 9:21:59 PM
1class Solution:
2    def invertTree(self, root):
3        if root is None:
4            return None
5        root.left, root.right = root.right, root.left
6        self.invertTree(root.left)
7        self.invertTree(root.right)
8
9        return root
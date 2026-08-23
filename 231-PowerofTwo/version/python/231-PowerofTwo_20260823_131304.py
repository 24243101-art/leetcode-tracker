# Last updated: 8/23/2026, 1:13:04 PM
1class Solution:
2    def lowestCommonAncestor(self, root, p, q):
3
4        while root:
5            if p.val < root.val and q.val < root.val:
6                root = root.left
7
8            elif p.val > root.val and q.val > root.val:
9                root = root.right
10
11            else:
12                return root
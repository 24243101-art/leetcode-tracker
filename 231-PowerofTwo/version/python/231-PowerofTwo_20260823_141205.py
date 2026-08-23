# Last updated: 8/23/2026, 2:12:05 PM
1class Solution:
2    def lowestCommonAncestor(self, root, p, q):
3
4        if root is None:
5            return None
6
7        if root == p or root == q:
8            return root
9
10        left = self.lowestCommonAncestor(root.left, p, q)
11        right = self.lowestCommonAncestor(root.right, p, q)
12
13        if left and right:
14            return root
15
16        if left:
17            return left
18        else:
19            return right
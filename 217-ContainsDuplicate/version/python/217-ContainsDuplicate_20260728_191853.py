# Last updated: 7/28/2026, 7:18:53 PM
1class Solution:
2    def countNodes(self, root):
3        if not root:
4            return 0
5
6        left = root
7        right = root
8
9        leftHeight = 0
10        rightHeight = 0
11
12        while left:
13            leftHeight += 1
14            left = left.left
15
16        while right:
17            rightHeight += 1
18            right = right.right
19
20        if leftHeight == rightHeight:
21            return (1 << leftHeight) - 1
22
23        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
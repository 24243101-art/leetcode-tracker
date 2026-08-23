# Last updated: 8/23/2026, 12:44:57 PM
1class Solution:
2    def kthSmallest(self, root, k):
3        stack = []
4        current = root
5
6        while True:
7            while current:
8                stack.append(current)
9                current = current.left
10
11            current = stack.pop()
12            k -= 1
13
14            if k == 0:
15                return current.val
16
17            current = current.right
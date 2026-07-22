# Last updated: 7/22/2026, 9:19:29 PM
1class BSTIterator:
2
3    def __init__(self, root):
4        self.stack = []
5        self.leftMost(root)
6
7    def leftMost(self, node):
8        while node:
9            self.stack.append(node)
10            node = node.left
11
12    def next(self):
13        node = self.stack.pop()
14        if node.right:
15            self.leftMost(node.right)
16        return node.val
17
18    def hasNext(self):
19        return len(self.stack) > 0
# Last updated: 8/23/2026, 4:58:33 PM
1class Solution:
2    def deleteNode(self, node):
3        node.val = node.next.val
4        node.next = node.next.next
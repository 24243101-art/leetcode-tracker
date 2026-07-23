# Last updated: 7/23/2026, 9:13:42 PM
1class Solution(object):
2    def removeElements(self, head, val):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        current = dummy
7
8        while current.next:
9            if current.next.val == val:
10                current.next = current.next.next
11            else:
12                current = current.next
13
14        return dummy.next
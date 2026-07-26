# Last updated: 7/26/2026, 7:59:20 PM
1
2class Solution:
3    def reverseList(self, head):
4        prev = None
5        curr = head
6
7        while curr:
8            nxt = curr.next
9            curr.next = prev
10            prev = curr
11            curr = nxt
12
13        return prev
# Last updated: 7/15/2026, 3:00:28 PM
1class Solution:
2    def insertionSortList(self, head):
3        dummy = ListNode(0)
4
5        curr = head
6
7        while curr:
8            next_node = curr.next
9
10            prev = dummy
11            while prev.next and prev.next.val < curr.val:
12                prev = prev.next
13
14            curr.next = prev.next
15            prev.next = curr
16
17            curr = next_node
18
19        return dummy.next
# Last updated: 7/15/2026, 3:04:51 PM
1class Solution:
2    def sortList(self, head):
3        if not head or not head.next:
4            return head
5
6        slow = head
7        fast = head.next
8
9        while fast and fast.next:
10            slow = slow.next
11            fast = fast.next.next
12
13        mid = slow.next
14        slow.next = None
15        left = self.sortList(head)
16        right = self.sortList(mid)
17        dummy = ListNode(0)
18        tail = dummy
19
20        while left and right:
21            if left.val < right.val:
22                tail.next = left
23                left = left.next
24            else:
25                tail.next = right
26                right = right.next
27            tail = tail.next
28
29        if left:
30            tail.next = left
31        else:
32            tail.next = right
33
34        return dummy.next
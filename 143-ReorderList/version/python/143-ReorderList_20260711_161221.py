# Last updated: 7/11/2026, 4:12:21 PM
1class Solution:
2    def reorderList(self, head):
3        if not head or not head.next:
4            return
5
6        slow = head
7        fast = head
8
9        while fast.next and fast.next.next:
10            slow = slow.next
11            fast = fast.next.next
12
13        second = slow.next
14        slow.next = None
15
16        prev = None
17        while second:
18            nxt = second.next
19            second.next = prev
20            prev = second
21            second = nxt
22
23        first = head
24        second = prev
25
26        while second:
27            t1 = first.next
28            t2 = second.next
29
30            first.next = second
31            second.next = t1
32
33            first = t1
34            second = t2
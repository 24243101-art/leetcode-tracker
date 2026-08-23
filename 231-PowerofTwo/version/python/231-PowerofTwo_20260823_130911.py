# Last updated: 8/23/2026, 1:09:11 PM
1class Solution:
2    def isPalindrome(self, head):
3        slow = head
4        fast = head
5
6        while fast and fast.next:
7            slow = slow.next
8            fast = fast.next.next
9        prev = None
10
11        while slow:
12            next_node = slow.next
13            slow.next = prev
14            prev = slow
15            slow = next_node
16        left = head
17        right = prev
18
19        while right:
20            if left.val != right.val:
21                return False
22
23            left = left.next
24            right = right.next
25
26        return True
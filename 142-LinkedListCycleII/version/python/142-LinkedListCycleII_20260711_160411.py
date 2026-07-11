# Last updated: 7/11/2026, 4:04:11 PM
1class Solution:
2    def detectCycle(self, head):
3        slow = head
4        fast = head
5
6        while fast and fast.next:
7            slow = slow.next
8            fast = fast.next.next
9
10            if slow == fast:
11                break
12        else:
13            return None
14
15        slow = head
16        while slow != fast:
17            slow = slow.next
18            fast = fast.next
19
20        return slow
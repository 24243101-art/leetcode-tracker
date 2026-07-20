// Last updated: 7/20/2026, 3:46:36 PM
1public class Solution {
2    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
3
4        ListNode p1 = headA;
5        ListNode p2 = headB;
6
7        while (p1 != p2) {
8            if (p1 == null) {
9                p1 = headB;
10            } else {
11                p1 = p1.next;
12            }
13
14            if (p2 == null) {
15                p2 = headA;
16            } else {
17                p2 = p2.next;
18            }
19        }
20
21        return p1;
22    }
23}
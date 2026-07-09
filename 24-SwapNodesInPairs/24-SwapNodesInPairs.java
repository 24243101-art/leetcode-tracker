// Last updated: 7/9/2026, 10:11:41 AM
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;
            first.next = second.next;
            second.next = first;
            prev.next = second;
            prev = first;
        }

        return dummy.next;
    }
}

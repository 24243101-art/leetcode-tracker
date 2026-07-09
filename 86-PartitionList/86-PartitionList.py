# Last updated: 7/9/2026, 10:09:26 AM
class Solution:
    def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next

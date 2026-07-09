# Last updated: 7/9/2026, 10:09:17 AM
class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        nxt = None
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        
        return dummy.next

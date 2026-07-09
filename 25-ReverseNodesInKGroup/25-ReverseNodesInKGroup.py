# Last updated: 7/9/2026, 10:11:40 AM
class Solution(object):
    def reverseKGroup(self, head, k):
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while count >= k:
            tail = curr
            for _ in range(k):
                tail = tail.next
            new_head = reverse(curr, tail)
            prev.next = new_head
            curr.next = tail
            prev = curr
            curr = tail
            count -= k

        return dummy.next

        
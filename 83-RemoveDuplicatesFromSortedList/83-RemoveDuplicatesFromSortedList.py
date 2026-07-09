# Last updated: 7/9/2026, 10:09:35 AM
class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  
            else:
                current = current.next
        return head

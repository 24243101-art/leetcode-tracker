# Last updated: 7/9/2026, 10:09:04 AM
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

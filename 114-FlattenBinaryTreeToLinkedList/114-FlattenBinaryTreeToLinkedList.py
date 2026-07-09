# Last updated: 7/9/2026, 10:08:38 AM
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        if not root:
            return        
        self.flatten(root.left)
        self.flatten(root.right)        
        temp = root.right        
        root.right = root.left
        root.left = None        
        curr = root
        while curr.right:
            curr = curr.right        
        curr.right = temp

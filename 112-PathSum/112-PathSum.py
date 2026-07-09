# Last updated: 7/9/2026, 10:08:41 AM
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))

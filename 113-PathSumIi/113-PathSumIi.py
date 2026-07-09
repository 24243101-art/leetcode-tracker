# Last updated: 7/9/2026, 10:08:39 AM
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        res = []

        def dfs(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val
            if not node.left and not node.right and total == targetSum:
                res.append(list(path))
            dfs(node.left, path, total)
            dfs(node.right, path, total)
            path.pop()

        dfs(root, [], 0)
        return res

        
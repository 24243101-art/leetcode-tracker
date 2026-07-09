# Last updated: 7/9/2026, 10:09:00 AM
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        
        return result

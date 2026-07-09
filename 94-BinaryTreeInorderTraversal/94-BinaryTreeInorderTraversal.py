# Last updated: 7/9/2026, 10:09:14 AM
class Solution:
    def inorderTraversal(self, root):
        result = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)       
            result.append(node.val)  
            inorder(node.right)     
        
        inorder(root)
        return result

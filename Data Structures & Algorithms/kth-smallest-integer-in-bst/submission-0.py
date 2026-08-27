# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def inOrder(root):
            if not root:
                return 
            
            inOrder(root.left)

            nonlocal count
            nonlocal result
       
            count+=1
            if count == k:
                result = root.val
                return result
            
            
            inOrder(root.right)
        inOrder(root)
        return result
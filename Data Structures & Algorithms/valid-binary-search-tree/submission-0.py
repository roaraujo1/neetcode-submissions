# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.check(float("-inf"),root,float('inf'))
    

    def check(self,low,node,high):
        if not node:
            return True

        if not(low < node.val<high):
            return False
        
        left = self.check(low,node.left,node.val)
        right = self.check(node.val,node.right,high)
        return left and right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {}

        for ind,val in enumerate(inorder):
            pos[val] = ind
        
        
        def create(start,inLeft,inRight):
            if inLeft > inRight:
                return None
        
            node = TreeNode(preorder[start])
            node.left = create(start+1,inLeft,pos[node.val]-1)
            node.right = create(start+1+pos[node.val]-inLeft,pos[node.val]+1,inRight)
            return node
        

        return create(0,0,len(preorder)-1)

        



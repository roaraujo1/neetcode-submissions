# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            len_queue = len(queue)
            level = []

            for i in range(len_queue):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                level.append(node.val)
            if level:
                res.append(level)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        while q:
            node = q.popleft()
            left, right = 0, 0
            if node.left:
                left = self.maxDept(node.left)
                q.append(node.left)
            if node.right:
                right = self.maxDept (node.right)
                q.append(node.right)
            if max(left, right) - min(left, right) > 1:
                return False
        return True

    def maxDept (self, root):
        if not root:
            return 0
        return 1 + max(self.maxDept(root.left) , self.maxDept(root.right))
        
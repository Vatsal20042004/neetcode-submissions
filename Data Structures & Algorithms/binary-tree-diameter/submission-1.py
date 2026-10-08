# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #split at root for the maximum dept at both sides and add them
        q = deque([root])
        diameter = 0
        while q:
            node = q.popleft()
            left_max = 0
            right_max = 0
            if node.left: 
                left_max = self.maxDept(node.left)
                q.append(node.left) 
            if node.right:
                right_max = self.maxDept(node.right)
                q.append(node.right)
            diameter = max(diameter, right_max + left_max)
        return diameter

    def maxDept(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDept(root.left),self.maxDept(root.right))


        
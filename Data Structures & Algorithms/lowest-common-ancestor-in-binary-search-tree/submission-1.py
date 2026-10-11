# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #this method looks similar like binary search
        low, high = min(p.val, q.val), max(p.val, q.val)

        node = root
        
        while node:
            if node.val < low:
                node = node.right
            elif node.val > high:
                node = node.left
            else:
                return node

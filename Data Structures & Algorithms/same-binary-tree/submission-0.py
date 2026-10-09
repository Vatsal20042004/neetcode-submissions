# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_q, q_q = deque([p]), deque([q])
        
        while p_q and q_q:
            node_p, node_q = p_q.popleft(), q_q.popleft()
            
            if not node_p and not node_q:
                continue
            if not node_p or not node_q:
                return False
            if node_p.val != node_q.val:
                return False
            
            p_q.append(node_p.left)
            p_q.append(node_p.right)
            q_q.append(node_q.left)
            q_q.append(node_q.right)

        return not p_q and not q_q

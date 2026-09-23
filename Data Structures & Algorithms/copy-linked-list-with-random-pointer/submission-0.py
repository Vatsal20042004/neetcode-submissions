"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        dummy = Node(0, None, None)

        # linked list and map construction
        ite = head
        prev = dummy
        addr = {}
        while ite:
            temp = Node(ite.val, None, None)
            prev.next = temp
            addr[ite] = temp
            prev = temp
            ite = ite.next
        
        #construction of random values
        ite = head
        while ite:
            if ite.random:
                addr[ite].random = addr[ite.random]
            ite = ite.next
        
        return dummy.next

        
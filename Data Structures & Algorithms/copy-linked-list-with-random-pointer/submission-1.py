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
        
        #creating copy nodes in the same linked list
        ite = head
        while ite:
            nxt = ite.next
            copy = Node(ite.val, nxt)
            ite.next = copy
            ite = nxt
        
        #creating random values as well
        ite = head
        while ite:
            if ite.random:
                ite.next.random = ite.random.next
            ite = ite.next.next
        
        #interleave the linkedlist
        cur, newhead = head, head.next
        while cur:
            copy = cur.next
            cur.next = copy.next
            copy.next = cur.next.next if cur.next else None
            cur = cur.next
        return newhead


        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        # find the total length
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length+=1
        index = length - n

        #delete the element using dummy 
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range (length - n):
            prev = prev.next
        prev.next = prev.next.next
        return  dummy.next
        

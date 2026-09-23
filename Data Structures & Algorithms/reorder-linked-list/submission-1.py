# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1=head
        temp=head
        length=0
        while temp:
            temp=temp.next
            length+=1
        half=(length+1)//2
        idx=0
        temp=head
        while idx<half-1:
            temp=temp.next
            idx+=1
        l2=temp.next
        temp.next=None
        prev=None
        while l2:
            nxt=l2.next
            l2.next=prev
            prev=l2
            l2=nxt
        l2=prev
        while l2:
            temp=l1.next
            l1.next=l2
            temp2=l2.next
            l2.next=temp
            l1=temp
            l2=temp2
        return

        
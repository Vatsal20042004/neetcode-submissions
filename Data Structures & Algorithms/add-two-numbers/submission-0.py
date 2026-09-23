# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = '', ''
        ite1, ite2 = l1, l2

        #appending the values in form of strings
        while ite1:
            num1 = num1 + str(ite1.val)
            ite1 = ite1.next
        
        while ite2:
            num2 = num2 + str(ite2.val)
            ite2 = ite2.next
        
        #reversing adding and forming new linkedlist
        num1,num2 = int(num1[::-1]), int(num2[::-1])
        res = str(num1+num2)
        res = res[::-1]

        dummy=ListNode(0, None)
        ite = dummy
        for char in res:
            temp=ListNode(int(char))
            ite.next = temp
            ite = ite.next
        return dummy.next




        
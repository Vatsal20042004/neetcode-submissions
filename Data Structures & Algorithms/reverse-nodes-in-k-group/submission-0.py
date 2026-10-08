class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1

        dummy = ListNode(0, head)
        ite = 0
        temp = dummy

        while ite + k <= length:
            e_dummy = ListNode()
            start = temp              
            last = temp.next          
            temp = temp.next

            for _ in range(k):
                next_temp = temp.next
                temp.next = e_dummy.next
                e_dummy.next = temp
                temp = next_temp      

            start.next = e_dummy.next 
            last.next = temp          
            temp = last               
            ite += k

        return dummy.next
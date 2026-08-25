# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        length = 0

        while curr:
            length+=1
            curr = curr.next
        
        pos = length-n
        if pos == 0:
            head = head.next
            return head

        curr = head
        i=0

        while curr:
            if i+1 == pos:
                curr.next = curr.next.next
            curr = curr.next
            i+=1
        
        return head
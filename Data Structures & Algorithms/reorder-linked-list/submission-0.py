# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        

        prev = None
        new_beg = slow.next

        while new_beg:
            nxt = new_beg.next
            new_beg.next = prev
            prev = new_beg
            new_beg = nxt

        slow.next = None

        curr = head
        while  prev:
            curr_nxt = curr.next
            prev_nxt = prev.next

            curr.next = prev
            prev.next = curr_nxt
            
            curr = curr_nxt
            prev = prev_nxt


        

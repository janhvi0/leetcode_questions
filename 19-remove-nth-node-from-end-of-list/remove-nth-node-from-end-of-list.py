# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # Step 2: Find the (L - n)th node (previous node of the target)
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        temp = dummy
        for _ in range(length - n):  
            temp = temp.next
        
        # Step 3: Remove the nth node
        temp.next = temp.next.next
        
        return dummy.next  # Return updated head

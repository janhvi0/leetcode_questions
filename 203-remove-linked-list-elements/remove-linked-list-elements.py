# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node before head
        dummy.next = head  # Point to the original list
        current = dummy  # Iterator starting from dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # Skip the node with value 'val'
            else:
                current = current.next  # Move to the next node
        
        return dummy.next  # Return the updated head










        # # if self.head.val==val:                     #edge case is val is in the head
        # #     self.head.val = self.head.next.val
        # #     self.head.next = self.head.next.next

        # dummy = ListNode(0)
        # dummy.next = head
        # current = dummy

        # while current.next:
        #     if current.next.val == val:
        #         current.next = current.next.next

        #     else:
        #         current = current.next

        # return dummy.next

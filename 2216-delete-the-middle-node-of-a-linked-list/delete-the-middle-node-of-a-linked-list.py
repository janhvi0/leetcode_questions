# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None  # Edge case: If the list has only one node, return None
        
        slow, fast = head, head
        prev = None  # To track the node before slow

        while fast and fast.next:
            prev = slow  # Store previous node
            slow = slow.next  # Move slow one step
            fast = fast.next.next  # Move fast two steps

        # Delete the middle node
        prev.next = slow.next
        
        return head  # Return modified list
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # if head==None and head.next==None:
        #     return head
        
        
        # fast=head
        # slow=head
        # prev=None

        # while fast!=None and fast.next!= None:
        #     prev=slow
        #     fast=fast.next.next
        #     slow=slow.next

        # prev.next=slow.next

        # return head

      
      
      
      
      
      
      
      
      
      
      
      
      
        # count=0
        # current=head
        # while current is not None:
        #     count+=1
        #     current = current.next

        # while current is not None and count==count//2:
        #     current.next=current.next.next
        # return head

 
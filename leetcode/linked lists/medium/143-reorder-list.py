# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        """
        # this is the optimal version which runs in linear time
        # reverse the second half of the list first
        
        # use fast and slow pointer to get the second half first
        
        ptr1 = head
        slow = head
        fast = slow.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        second = slow.next
        prev = slow.next = None
      
        while second:        
            third = second.next
            second.next = prev
            prev = second
            second = third
            
        # after this loop the list will be divided like so [1->2->3->None] and [None<-4-<5] 
        # ptr 1 will be at 1 and ptr 2 will be at 5
                                       
        ptr2 = prev
        
        while ptr1 and ptr2:
            
            nextnode = ptr1.next
            prevnode = ptr2.next
            
            ptr1.next = ptr2
            ptr1 = nextnode
            ptr2.next = ptr1
            
            ptr2 = prevnode
            
             
#         this is the brute force version which runs in quadratic time
#         left = head
        
#         if not left.next:
#             return left
        
#         while left.next.next:
#             right = left
#             nextnode = left.next
            
#             while right.next.next:    
#                 right = right.next
            
#             tail = right.next
            
#             left.next = tail
#             tail.next = nextnode
            
#             right.next = None
#             left = nextnode
            
#             if left.next == None:
#                 break

            
            
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        # the reason to create a dummy is because it covers all the edge cases(eg: list containing single node)
        
        dummy = ListNode()      # create a dummy node to set the left pointer at one position 
        dummy.next = head       # behind the target node
        head = dummy            # set new head to the dummy
        
        l = head                
        r = head.next
        for i in range(n):      # keep a distance of n between left and right pointer (this is the most IMP step)
            r = r.next          
        
        while r:                # while right exists increment both pointers by one
            l = l.next          # after loop ends right will be null always and left will be one position
            r = r.next          # behind the node to be deleted
            
        unwantednode = l.next   # remove the node
        l.next = unwantednode.next  
        return head.next
    
    
    
    
        
        
        
        
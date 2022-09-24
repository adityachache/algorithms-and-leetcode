# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        if not head:
            return None
        if not head.next:
            return head
        
        list1 = ListNode()
        ptr1 = list1
        
        list2 = ListNode()
        ptr2 = list2
        
        curr = head
        
        while curr:
            if curr.val < x:
                ptr1.next = curr
                ptr1 = ptr1.next
            else:
                ptr2.next = curr
                ptr2 = ptr2.next     
            curr = curr.next
            
        #After this loop list1 will be 
        # 0->1->2->2 and list2 will be
        # 0->4->3->5->2 the 2 at the end because when we do ptr2.next = curr the 5 will be curr at that time and it will be pointing 
        # towards 2
            
        # set the end as None
        ptr2.next = None
        
        # merge the two lists
        ptr1.next = list2.next     
        return list1.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = "" 
        num2 = ""
        total = 0
        
        cur1 = l1
        cur2 = l2
        
        while cur1:
            num1 += str(cur1.val)
            cur1 = cur1.next
        
        while cur2:
            num2 += str(cur2.val)
            cur2 = cur2.next
            
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        
        total = str(num1 + num2)
        total = total[::-1]
        
        head = ListNode()
        cur = head
        
        for i in total:
            
            digit = ListNode(val=int(i))
            cur.next = digit
            cur = cur.next
            
        
        return head.next
            
        
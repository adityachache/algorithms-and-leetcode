# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        myhash = {} 
    
        l1 = headA
        l2 = headB
        
        while l1:               # store all the nodes in a hash table since we don't know on which node
            myhash[l1] = 1      # the second list is gonna intersect
            l1 = l1.next
            
        while l2:
            if l2 in myhash:    # loop through the second list and if it contains any node that's in the 
                return l2       # hash table then return that node.
            l2 = l2.next
        
        return None             # if you don't find any node in hash table then return None since the 
                                # second list doesn't intersect the first
      


# O(1) space complexity approach  
# first = headA
#         second = headB
        
#         length1 = 0
#         length2 = 0
        
        
#         while first:
#             length1 += 1
#             first = first.next
            
#         while second:
#             length2 += 1
#             second = second.next
            
#         if first != second:
#             return None
#         else:
            
#             first = headA
#             second = headB
            
#             if length1 > length2:
#                 diff = length1 - length2
#                 for i in range(diff):
#                     first = first.next 
#             else:
#                 diff = length2 - length1
#                 for i in range(diff):
#                     second = second.next
                    
#             while first!= second:
#                 first =first.next
#                 second = second.next
                
#             return first

        
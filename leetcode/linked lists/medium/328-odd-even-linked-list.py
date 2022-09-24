# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head:
            return None
        else:
            newlist1 = ListNode()           # list 1 to store all the odd indexed nodes
            newlist2 = ListNode()           # list 2 to store all the even indexed nodes

            curr_node1 = newlist1           # set head to add nodes list 1
            curr_node2 = newlist2           # set head to add nodes list 2
            
            left = head                     # set left pointer for odd nodes
            right = head.next               # set right pointer for even nodes
            
            while right and right.next:           # loop till the right pointer and next exists
                curr_node1.next = left            # add odd nodes to list 1
                curr_node2.next = right           # even nodes to list 2
                
                left = left.next.next             # increment left and right pointers by 2 
                right = right.next.next           # since we want odd and even nodes
                
                curr_node1 = curr_node1.next      # increment the list nodes
                curr_node2 = curr_node2.next

            curr_node1.next = left                # the last elements won't get added so add that to both
            curr_node1 = curr_node1.next          # the lists after loop ends
            curr_node2.next = right              
            curr_node2 = curr_node2.next
            
            curr_node1.next = newlist2.next       # finally set the next pointer of list1 to entire list2
    
            return newlist1.next                  # return list1
    
                
        
        
        # for eg:- let's consider the list [1,2,3,4,5,6]
        # in this example we first set our left and right pointers which will be at 1(odd) and 2(even)      respectively
        # After that we loop till right and right.next exists 
        
        # Iteration 1:- 1 will be added to list1 and 2 will be added to list2
        
        # Iteration 2:- 3, 4 will be added to the lists
        
        # Iteration 3:-  loop will be terminated because right.next doesn't exists
        
        # so after exiting the loop we still have to add 5, 6 and we do that in lines 32-35
        
        # Space complexity is O(N) and time complexity is O(N)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
             
            
        if not root:
            return []
        else:
            val_arr = []
            queue = collections.deque()
            currentnode = root
            queue.appendleft(currentnode)
           
            while (len(queue) > 0):
                
                newlist = []
                for i in range(len(queue)):
                    currentnode = queue.pop() 

                    if currentnode.left:
                        queue.appendleft(currentnode.left)

                    if currentnode.right:
                        queue.appendleft(currentnode.right)

                    newlist.append(currentnode.val)
                    
                val_arr.append(newlist)
                
            return val_arr
                
        
        
        
        
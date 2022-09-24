# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        #iterative 
        if not root:
            return []
        else:
            val_arr = []
            stack = []
            currentnode = root
        
            stack.append(currentnode)
            
            while (len(stack) > 0):
                currentnode = stack.pop()
                val_arr.append(currentnode.val)
                
                if currentnode.right:
                    stack.append(currentnode.right)
                
                if currentnode.left:
                    stack.append(currentnode.left)

            return val_arr
        
        

#         #recursive 
#         if not root:
#             return []
#         else:
#             val_arr = []  
#             val_arr.append(root.val)
#             if root.left:      
#                 val_arr += self.preorderTraversal(root.left)
#             if root.right:
#                 val_arr += self.preorderTraversal(root.right)

#             return val_arr
                
            
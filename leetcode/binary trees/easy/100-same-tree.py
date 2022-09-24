# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
          
        # check if both are null nodes
        if not p and not q:
            return True

        # check if they both exists and their node values match
        if p and q and (p.val == q.val):

            # call recursively on left and right nodes of both trees
            res = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            return res

        # if any one tree exists or node values doesn't match
        return False
        
               
        # My approach
#         def dfs_p(root1, val_arr1):
            
#             if not root1:
#                 val_arr1.append(0)
#                 return 0
            
#             val_arr1.append(root1.val)          # traverse first tree and add all node values in array 1
            
#             dfs_p(root1.left, val_arr1)
#             dfs_p(root1.right, val_arr1)
            
#             return val_arr1
        
        
#         def dfs_q(root2, val_arr2):
            
#             if not root2:
#                 val_arr2.append(0)
#                 return 0
#                                                 # traverse second tree and add all node values in array 2
#             val_arr2.append(root2.val)
            
#             dfs_p(root2.left, val_arr2)
#             dfs_p(root2.right, val_arr2)
            
#             return val_arr2
        
          
#         left = dfs_p(p,[])
#         right = dfs_q(q,[])
        
#         return left == right                    # check if both the arrays are the same
            
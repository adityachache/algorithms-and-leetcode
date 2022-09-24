# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        currentnode = root
        
        while currentnode:
            
            # if both values are greater than root then check the right half
            if p.val > currentnode.val and q.val > currentnode.val:
                currentnode = currentnode.right
                
            # if both values are smaller than root then check the left half
            elif p.val < currentnode.val and q.val < currentnode.val:
                currentnode = currentnode.left
        
            
            # if both of the above statements doesn't execute that means that we've encountered a split so we return root
            else:
                return currentnode

        
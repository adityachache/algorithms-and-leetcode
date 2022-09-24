# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # my approach O(N)
#         if not root:
#             return 0
#         else:
#             left_depth = 1
#             right_depth = 1
#             max_depth = 1
            
#             if root.left:
#                 left_depth += self.maxDepth(root.left)
                     
#             if root.right:
#                 right_depth += self.maxDepth(root.right)

            
#             max_depth = max(left_depth, right_depth)
            
#             return max_depth
            
        if not root:
            return 0 
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
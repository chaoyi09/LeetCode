# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = self.helper(root)
        return result[0] if result else True
    
    def helper(self, root):
        if root is None:
            return True, 0
        
        left_balanced, left_depth = self.helper(root.left)
        right_balanced, right_depth = self.helper(root.right)
        
        if not left_balanced or not right_balanced:
            return False, -1
        
        balanced = abs(left_depth - right_depth) <= 1
        depth = max(left_depth, right_depth) + 1
        return balanced, depth
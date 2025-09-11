class Solution:
    def isValidBST(self, root: 'TreeNode') -> bool:
        def dfs(node, low, high) -> bool:
            if node is None:
                return True
            if (low is not None and node.val <= low) or \
               (high is not None and node.val >= high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, None, None)
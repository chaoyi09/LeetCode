# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []

        def dfs(node, r, c):
            if not node:
                return
            nodes.append((c, r, node.val))
            dfs(node.left,  r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)

        dfs(root, 0, 0)
        nodes.sort()

        ans, cur_col, cur_bucket = [], None, []
        for c, r, v in nodes:
            if c != cur_col:
                if cur_bucket:
                    ans.append(cur_bucket)
                cur_col = c
                cur_bucket = [v]
            else:
                cur_bucket.append(v)
        if cur_bucket:
            ans.append(cur_bucket)
        return ans

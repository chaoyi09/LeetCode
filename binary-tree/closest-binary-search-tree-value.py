# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        cur = root
        while cur:
            # 更近则更新；相等距离时取较小值
            if (abs(cur.val - target) < abs(ans - target)) or \
               (abs(cur.val - target) == abs(ans - target) and cur.val < ans):
                ans = cur.val

            # Using BST properties to determine direction
            if target < cur.val:
                cur = cur.left
            elif target > cur.val:
                cur = cur.right
            else:
                return cur.val
        return ans

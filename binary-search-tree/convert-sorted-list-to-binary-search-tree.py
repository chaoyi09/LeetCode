# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        self.ptr = head

        def build(l:int, r: int) -> Optional[TreeNode]:
            if l > r :
                return None

            m = (l + r) // 2
            left = build(l, m - 1)
            root = TreeNode(self.ptr.val)
            self.ptr = self.ptr.next
            root.left = left
            root.right = build(m + 1, r)
            return root
        return build(0, n -1)